from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

items = ["Apple", "Banana", "Orange", "Grapes", "Mango"]

@app.get("/")
async def read_items(request: Request):
    return templates.TemplateResponse("items.html", {"request": request, "items": items})
