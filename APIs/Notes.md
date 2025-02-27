# APIs Notes

## Concepts to Learn
- Understanding API client programming and endpoint development.
- Developing simple APIs using FastAPI.
- Building Streamlit applications for API interaction.

## Tasks & Approaches

### API Client Programming
Developing API clients to interact with external APIs and handle responses efficiently.

### API Endpoint Development
Building robust API endpoints using FastAPI and understanding request/response cycles.

### Simple FastAPI Development
Creating basic FastAPI applications, defining routes, handling parameters, and responses.

### Simple API Development
Building simple APIs with authentication, CRUD operations, and middleware handling.

### Streamlit Applications
Creating interactive applications using Streamlit to visualize API responses.

## Errors Faced & Solutions

### Error 1: "Error loading ASGI app. Could not import module 'main'"
**Solution:**
- Ensure that `main.py` exists in the directory.
- Verify the module name in the Uvicorn command:
  ```sh
  uvicorn main:app --reload
  ```
- Check for any syntax errors in `main.py`.
- Ensure FastAPI is installed correctly using:
  ```sh
  pip install fastapi uvicorn
  ```

## What I Learned
- The structure of API development using FastAPI.
- How to debug and fix common issues in FastAPI applications.
- Building interactive API-driven applications with Streamlit.

## ChatGPT Assistance
For further assistance, refer to [ChatGPT](https://chatgpt.com/share/67bb315a-66a0-8004-9c50-f07abc4fc562).
