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
