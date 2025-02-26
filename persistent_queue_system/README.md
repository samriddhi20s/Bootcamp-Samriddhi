# Persistent Queue System

## Overview
The Persistent Queue System is a robust producer-consumer system designed to handle job submissions and processing reliably. It ensures that jobs are persisted across application restarts and can handle multiple producers and consumers. The system is designed to be fault-tolerant, with mechanisms to handle consumer crashes and problematic jobs.


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
   - Manages the producer and consumer processes.

## Problem Description
In distributed systems, ensuring reliable job processing is a common challenge. Producers submit jobs to a queue, and consumers process them. However, issues such as consumer crashes, problematic jobs, and system restarts can lead to job loss or duplication. This project addresses these challenges by implementing a persistent queue system that:
- Persists jobs across application restarts.
- Handles consumer crashes gracefully.
- Detects and manages problematic jobs.
- Abstracts the database implementation for future extensibility.
  
## Usage Instructions
- Install dependencies: `pip install -r requirements.txt`
- Run producers: `python3 -m producer.py`
- Run consumers: `python3 -m consumer.py`
- Run Ops console: `streamlit run ops_console.py`
- Run Admin console: `streamlit run admin_console.py`

## Task Flow
```mermaid
graph TD
    Producer -->|Submit Job| Queue
    Queue -->|Dequeue Job| Consumer
    Consumer -->|Acknowledge| Queue
    Consumer -->|Crash| Queue
    Queue -->|Requeue Job| Consumer
    Queue -->|Move to Dead Letter| DeadLetterQueue
