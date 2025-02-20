from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the "static" directory for serving files
app.mount("/static", StaticFiles(directory="static"), name="static")

#  Example API route
@app.get("/")
def root():
    return {"message": "FastAPI Static File Serving Example"}

