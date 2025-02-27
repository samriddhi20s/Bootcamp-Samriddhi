# FastAPI Endpoint Development

## Overview
This project demonstrates FastAPI development with template rendering and basic authentication.

## Features
1. **Template Rendering**:
   - Uses Jinja2 templates to dynamically render an HTML page displaying a list of items.
2. **Basic Authentication**:
   - Implements basic authentication for a secured route using a username and password.

## Requirements
- Python 3.8+
- FastAPI
- Jinja2
- Uvicorn

## Installation
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <project_directory>
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install fastapi jinja2 uvicorn
   ```

## Usage
### Start the FastAPI server:
```sh
uvicorn main:app --reload
```

### Template Rendering
- The root endpoint (`/`) serves an HTML page displaying a list of items dynamically.
- Uses Jinja2 templates for rendering.

### Basic Authentication
- A protected route (`/secure`) requires authentication.
- Username and password need to be provided in the request.

## Expected Output
1. A webpage displaying dynamic content.
2. A secured route accessible only with valid credentials.

## Project Structure
```
/your_project_directory
│── main.py
│── templates/
│   └── index.html
│── static/
│── README.md
```


