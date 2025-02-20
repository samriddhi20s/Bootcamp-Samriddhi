from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()

# 📌 Simulated Email Sending Function (Runs in Background)
def send_email(email: str, message: str):
    time.sleep(3)  # Simulating email processing delay
    print(f"📧 Email sent to {email}: {message}")

# ✅ API Endpoint to Trigger Email Sending
@app.post("/send-notification/")
def send_notification(email: str, message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, message)
    return {"message": "Notification is being sent in the background!"}

# ✅ Root Endpoint
@app.get("/")
def root():
    return {"message": "FastAPI Background Task Example"}
