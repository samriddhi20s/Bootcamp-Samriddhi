# Persistent Queue System

## Overview
This project implements a producer-consumer system with a persistent queue that survives application restarts. The system supports multiple producers and consumers, ensuring robustness and job persistence.

## System Design
- **Producer**: Submits jobs to the queue.
- **Consumer**: Processes jobs from the queue.
- **Ops**: Monitors job status and details.
- **Admin**: Manages queue operations like resubmitting or canceling jobs.

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