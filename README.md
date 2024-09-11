# Notion2json - Convert Markdown to JSON

This project is a Streamlit-based web app that parses Markdown content into a structured JSON format. The application reads Markdown input, processes it using Python libraries, and displays the JSON representation of the content, maintaining the hierarchy and components such as text, video, habits, and more.

## Features

- **Dynamic Markdown Input**: Input your Markdown content and get an instant JSON representation.
- **Component Parsing**: The app identifies various components such as `VIDEO`, `TEXT`, `INPUT`, `HABIT`, etc., and formats them into structured JSON.
- **Side-by-side Layout**: The interface provides a responsive layout with Markdown input on the left and JSON output on the right.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Requirements

- Python 3.x
- Streamlit
- BeautifulSoup4
- Markdown


The dependencies are listed in the `requirements.txt` file. You can install them by running:

```bash
pip install -r requirements.txt
```


## Sample Input
```markdown
# Module Title
Welcome to the module introduction.

## Lesson 1: Introduction to Markdown
Markdown is a lightweight markup language.

### Page 1: What is Markdown?
Markdown is a text-to-HTML conversion tool for web writers.

This is a simple paragraph explaining markdown.

::activity::text_entry
<div>
label: Activity 1
placeholder: Enter your answer here
variable: activity1
</div>

::activity::calendar_input
<div>
label: Activity 2
placeholder: Select a date
variable: activity2
</div>

::activity::checkbox
<div>
label: Activity 3
variable: activity3
Options:
- Option 1
- Option 2
- Option 3
</div>


- List item 1
- List item 2
- List item 3

::video::
<div>
title: Introduction to AI
url: https://example.com/video/intro-to-ai
transcript: This video covers the basics of AI. It includes definitions and examples. It also discusses real-world applications.
</div>

::habit::
<div>
placeholder: Learn more about AI.
</div>

## Lesson 2: Markdown Syntax
Markdown uses plain text formatting.

### Page 1: Headers

::video::
<div>
title: Video Title
url: https://example.com/video.mp4
transcript: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</div>

```
