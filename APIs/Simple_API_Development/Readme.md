# Simple API Development with FastAPI

## Overview
This project covers fundamental FastAPI development concepts, including creating a basic API, handling CRUD operations, managing parameters, utilizing Pydantic models, integrating a database, and more.

## Features
1. **Hello World API**
   - Implements a basic FastAPI app returning "Hello, World!" on the root path.
2. **CRUD Operations**
   - Provides routes for creating, reading, updating, and deleting items using an in-memory data structure.
3. **Path and Query Parameters**
   - Supports dynamic routing with path parameters and filtering using query parameters.
4. **Request Body and Pydantic Models**
   - Utilizes Pydantic models for data validation and structuring request payloads.
5. **Database Integration**
   - Connects FastAPI with an SQLite database for persistent CRUD operations.
6. **Background Tasks**
   - Implements background task functionality, such as sending email notifications asynchronously.
7. **File Uploads**
   - Enables users to upload files and saves them to a designated directory.
8. **Serving Static Files**
   - Configures FastAPI to serve static files like images and HTML documents.

## Requirements
- Python 3.8+
- FastAPI
- Pydantic
- Uvicorn
- SQLite3

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
   pip install fastapi pydantic uvicorn sqlite3
   ```

## Usage
### Start the FastAPI server:
```sh
uvicorn main:app --reload
```

### Features Demonstrated
- Accessing `/` returns **"Hello, World!"**.
- CRUD operations available at `/items` endpoint.
- Query and path parameters for item filtering and retrieval.
- Uses Pydantic models for structured request validation.
- SQLite database integration for persistent storage.
- Background tasks for processing actions asynchronously.
- File uploads and serving static content enabled.

## Project Structure
```
/your_project_directory
│── main.py
│── database.py
│── models.py
│── templates/
│── static/
│── README.md
```

