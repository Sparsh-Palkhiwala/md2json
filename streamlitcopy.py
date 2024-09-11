import json
import markdown
from bs4 import BeautifulSoup
from enum import Enum
import streamlit as st

class componentenum(Enum):
    VIDEO = "VIDEO"
    TEXT = "TEXT"
    INPUT = "INPUT"
    HABIT = "HABIT"
    CHECKBOX = "CHECKBOX"
    MULTIPLE_CHOICE = "MULTIPLE_CHOICE"
    CALENDAR = "CALENDAR"

def parse_markdown_to_json(markdown_content):
    html_content = markdown.markdown(markdown_content)
    soup = BeautifulSoup(html_content, 'html.parser')

    modules = []
    current_module = None
    current_lesson = None
    current_page = None

    for element in soup.find_all(['h1', 'h2', 'h3', 'p', 'ol', 'li', 'a', 'iframe', 'div']):
        if element.name == 'h1':
            if current_page and current_page['components']:
                current_lesson["pages"].append(current_page)
                current_page = None
            if current_lesson:
                current_module["lessons"].append(current_lesson)
                current_lesson = None
            if current_module:
                modules.append(current_module)
            current_module = {
                "title": element.get_text(strip=True),
                "color": "#8ED6ED",
                "icon": {
                    "name": "Module Icon",
                    "url": "some_icon_url",  # Update with actual icon URL
                    "alt": "Module Icon Alt",
                    "category": "Module Category"  # Update with module category     
                },
                "lessons": []
            }
        elif element.name == 'h2':
            if current_page and current_page['components']:
                current_lesson["pages"].append(current_page)
                current_page = None
            if current_lesson:
                current_module["lessons"].append(current_lesson)
                current_lesson = None
            current_lesson = {
                "title": element.get_text(strip=True),
                "icon": {
                    "name": "Lesson Icon",
                    "url": "some_icon_url",  # Update with actual icon URL
                    "alt": "Lesson Icon Alt"
                },
                "pages": []
            }
        elif element.name == 'h3':
            if current_page and current_page['components']:
                current_lesson["pages"].append(current_page)
            current_page = {
                "title": element.get_text(strip=True),
                "components": []
            }
        elif element.name == 'p' and element.get_text(strip=True).startswith('::activity::'):
            if current_page is not None:
                activity_info = element.find_next('div')
                if activity_info:
                    activity_lines = activity_info.get_text(strip=True).split('\n')
                    activity_content = {}
                    for line in activity_lines:
                        if ':' in line:
                            key, value = line.split(':', 1)
                            key = key.strip().lower()
                            value = value.strip()
                            if key != "type":
                                activity_content[key] = value
                    current_page["components"].append({
                        'type': componentenum.INPUT.value,
                        'content': activity_content
                    })
        elif element.name == 'p' and element.get_text(strip=True).startswith('::video::'):
            if current_page is not None:
                video_info = element.find_next('div')
                if video_info:
                    video_content = {}
                    for line in video_info.get_text('\n').split('\n'):
                        if ':' in line:
                            key, value = line.split(':', 1)
                            key = key.strip().lower()
                            value = value.strip()
                            if key in ["title", "url", "transcript"]:
                                video_content[key] = video_content.get(key, '') + value + '\n' if key == "transcript" else value
                    video_content["transcript"] = video_content["transcript"].strip()  # Remove extra newlines
                    current_page["components"].append({
                        'type': componentenum.VIDEO.value,
                        'content': video_content
                    })
        elif element.name == 'p' and element.get_text(strip=True).startswith('::habit::'):
            if current_page is not None:
                habit_info = element.find_next('div')
                if habit_info:
                    habit_content = {}
                    for line in habit_info.get_text('\n').split('\n'):
                        if ':' in line:
                            key, value = line.split(':', 1)
                            key = key.strip().lower()
                            value = value.strip()
                            if key == "placeholder":
                                habit_content['habit_placeholder'] = value
                    current_page["components"].append({
                        'type': componentenum.HABIT.value,
                        'content': habit_content
                    })
        elif element.name == 'p':
            if current_page is not None:
                current_page["components"].append({
                    'type': componentenum.TEXT.value,
                    'content': {
                        'text': element.get_text(strip=True)
                    }
                })
        elif element.name == 'ol':
            if current_page is not None:
                list_items = [li.get_text(strip=True) for li in element.find_all('li')]
                current_page["components"].append({
                    'type': componentenum.TEXT.value,
                    'content': {
                        'text': '\n'.join(list_items)
                    }
                })

    if current_page and current_page['components']:
        current_lesson["pages"].append(current_page)
    if current_lesson:
        current_module["lessons"].append(current_lesson)
    if current_module:
        modules.append(current_module)

    return modules

import streamlit as st
import json

# Set page configuration to use wide layout and full-screen mode
st.set_page_config( layout="wide", 
                    page_title="Notion2json",
                    page_icon="🦉",
                    initial_sidebar_state="auto",
                    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
        }
    )

# Create two adaptive columns for side-by-side layout with a dynamic width ratio
# Left column for input will take 40% width, right column for output will take 60% width
col1, col2 = st.columns([0.45, 0.55])  # Adjusting the ratio for a responsive layout

# Left column: Markdown input
with col1:
    st.header("Markdown Input")
    markdown_input = st.text_area("Enter your markdown content", height=500)

# Right column: JSON Output
with col2:
    st.header("Parsed JSON Output")
    if markdown_input:
        json_data = parse_markdown_to_json(markdown_input)
        formatted_json = json.dumps(json_data, indent=2)
        st.code(formatted_json, language="json")



