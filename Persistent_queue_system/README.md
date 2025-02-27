# Persistent Queue System

## Overview
The Persistent Queue System is a robust producer-consumer system designed to handle job submissions and processing reliably. It ensures that jobs are persisted across application restarts and can handle multiple producers and consumers. The system is designed to be fault-tolerant, with mechanisms to handle consumer crashes and problematic jobs.

## Problem Description
In distributed systems, ensuring reliable job processing is a common challenge. Producers submit jobs to a queue, and consumers process them. However, issues such as consumer crashes, problematic jobs, and system restarts can lead to job loss or duplication. This project addresses these challenges by implementing a persistent queue system that:
- Persists jobs across application restarts.
- Handles consumer crashes gracefully.
- Detects and manages problematic jobs.
- Abstracts the database implementation for future extensibility.
- 
## System Design
The system consists of the following components:

### 1. **Producer**
- Submits jobs to the queue.
- Generates random files and enqueues their paths as jobs.

### 2. **Consumer**
- Processes jobs from the queue.
- Simulates processing delays and handles crashes gracefully.

### 3. **Queue**
- Manages job persistence and retrieval.
- Abstracts the database implementation (e.g., SQLite).
- Handles job acknowledgment, requeuing, and dead letter queue management.

### 4. **Ops Console**
- A Streamlit-based interface to monitor job statuses (pending, completed, failed).

### 5. **Admin Console**
- A Streamlit-based interface to manage the queue (e.g., resubmit failed jobs, view dead letter queue).

### 6. **Supervisor**
- Manages and monitors the producer, consumer, and console processes.
- Ensures processes are restarted automatically if they crash.


## Usage Instructions
- Install dependencies: `pip install -r requirements.txt`
- Run producers: `python3  producer.py`
- Run consumers: `python3  consumer.py`
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
