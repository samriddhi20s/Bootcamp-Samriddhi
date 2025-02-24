# Persistent Queue System

## Overview
This project implements a **producer-consumer system** with a **persistent queue** that survives application restarts. The system supports multiple producers and consumers, ensuring robustness and job persistence. Jobs are stored in an SQLite database, and the system includes monitoring and management consoles built with Streamlit.

## System Design
- **Producer**: Submits jobs to the queue.
- **Consumer**: Processes jobs from the queue.
- **Ops**: Monitors job status and details.
- **Admin**: Manages queue operations like resubmitting or canceling jobs.

The system consists of the following components:

1. **Producer:**
   - Submits jobs to the queue.
   - Generates random files and enqueues them as jobs.

2. **Consumer:**
   - Processes jobs from the queue.
   - Adds timestamps to files and marks jobs as processed.

3. **Persistent Queue:**
   - Manages the queue using an SQLite database.
   - Ensures jobs are persisted and can survive application restarts.

4. **Ops Console:**
   - A Streamlit-based console to monitor job status and details.

5. **Admin Console:**
   - A Streamlit-based console to manage the queue (e.g., resubmit or cancel jobs).

6. **Supervisor:**
   - Manages the producer and consumer processes (optional).

## Usage Instructions
- Install dependencies: `pip install -r requirements.txt`
- Run producers: `python -m producer`
- Run consumers: `python -m consumer`
- Run Ops console: `streamlit run ops_console.py`
- Run Admin console: `streamlit run admin_console.py`

## Task Flow
```mermaid
graph TD
    A[Producer] --> B[Queue]
    B --> C[Consumer]
    C --> D[Processed Jobs]
    B --> E[Ops Console]
    B --> F[Admin Console]
