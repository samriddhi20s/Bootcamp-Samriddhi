# Persistent Queue System - Project Notes

## Overview
The **Persistent Queue System** is a robust, file-based queue system designed to ensure message persistence, fault tolerance, and scalability. It includes a **Producer** to enqueue messages, a **Consumer** to dequeue messages, and two Streamlit-based interfaces: an **Ops Console** for queue operations and an **Admin Console** for system monitoring and management. The system also integrates a **FastAPI** backend for programmatic access and uses **SQLite** for persistent storage.

## Project Structure
 1. **`api.py`**
- **Functionality**: Implements the FastAPI backend for programmatic access to the queue system.
- **Key Features**:
  - RESTful endpoints for enqueueing and dequeueing messages.
  - Integration with the `persistent_queue` module for queue operations.
  - Example endpoints:
    - `POST /enqueue`: Enqueues a message into a specified queue.
    - `GET /dequeue`: Dequeues a message from a specified queue.

### 2. **`persistent_queue/`**
#### a. **`__init__.py`**
- **Functionality**: Initializes the `persistent_queue` module and makes its components accessible.

#### b. **`interfaces.py`**
- **Functionality**: Defines abstract base classes (ABCs) for queue interfaces.
- **Key Contributions**:
  - Provides a blueprint for implementing different types of queues (e.g., SQLite-based, file-based).

#### c. **`sqlite_queue.py`**
- **Functionality**: Implements a SQLite-based persistent queue.
- **Key Features**:
  - Stores messages and metadata in an SQLite database.
  - Ensures durability and atomicity of queue operations.

#### d. **`queue.py`**
- **Functionality**: Implements the core queue logic.
- **Key Features**:
  - Manages message enqueueing and dequeueing.
  - Integrates with the persistence layer (e.g., SQLite).

#### e. **`dead_letter_queue.py`**
- **Functionality**: Handles messages that cannot be processed after multiple retries.
- **Key Features**:
  - Moves failed messages to a dead-letter queue for further inspection.

#### f. **`models.py`**
- **Functionality**: Defines data models for the queue system.
- **Key Contributions**:
  - Includes models for messages, queues, and metadata.

#### g. **`utils.py`**
- **Functionality**: Provides utility functions for the queue system.
- **Key Features**:
  - Helper functions for file operations, database queries, and error handling.

### 3. **`scripts/`**
#### a. **`setup_db.py`**
- **Functionality**: Initializes the SQLite database and creates necessary tables.
- **Key Contributions**:
  - Ensures the database is ready for use by the queue system.

#### b. **`simulate_crash.py`**
- **Functionality**: Simulates system crashes to test fault tolerance and recovery.
- **Key Contributions**:
  - Helps validate the system's ability to recover from failures.

### 4. **`producer.py`**
- **Functionality**: Enqueues messages into the queue.
- **Key Features**:
  - Uses the `persistent_queue` module to add messages to the queue.
  - Ensures messages are persisted to the SQLite database.

### 5. **`consumer.py`**
- **Functionality**: Dequeues messages from the queue.
- **Key Features**:
  - Uses the `persistent_queue` module to retrieve and process messages.
  - Marks messages as processed or moves them to the dead-letter queue if they fail.

### 6. **`ops_console.py`**
- **Functionality**: Provides a Streamlit-based interface for queue operations.
- **Key Features**:
  - Allows users to enqueue and dequeue messages interactively.
  - Displays real-time feedback for each operation.

### 7. **`admin_console.py`**
- **Functionality**: Provides a Streamlit-based interface for system monitoring and management.
- **Key Features**:
  - Displays queue metrics (e.g., number of messages, queue size).
  - Monitors system health (e.g., disk usage, database status).
  - Allows administrators to create or delete queues.

### 8. **`supervisord.conf`**
- **Functionality**: Configuration file for Supervisord, a process control system.
- **Key Contributions**:
  - Manages and monitors the queue system processes (e.g., producer, consumer).

### 9. **`requirements.txt`**
- **Functionality**: Lists all Python dependencies for the project.
- **Key Contributions**:
  - Ensures easy setup and reproducibility of the project environment.

### 10. **`README.md`**
- **Functionality**: Provides an overview of the project, setup instructions, and usage guidelines.
- **Key Contributions**:
  - Helps users understand and use the project effectively.

## Key Features
- **Message Persistence**: Messages are stored in an SQLite database for durability.
- **Fault Tolerance**: Handles system crashes and ensures message recovery.
- **Streamlit Interfaces**: Provides user-friendly interfaces for queue operations and monitoring.
- **Programmatic Access**: Exposes RESTful APIs via FastAPI for integration with other systems.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `FastAPI`: For building RESTful APIs.
  - `Streamlit`: For building web-based interfaces.
  - `SQLite`: For persistent storage of messages and metadata.
  - `Supervisord`: For process management and monitoring

## Problems Faced
1. **SQLite Database Path**:
   - Initially faced issues with the `db_path` due to missing directories or invalid paths.
   - **Solution**: Fixed by ensuring the directory exists using `os.makedirs`.

2. **Supervisor Configuration**:
   - Encountered errors like `UNKNOWN_METHOD` and port conflicts.
   - **Solution**: Resolved by adding the `[rpcinterface:supervisor]` section and ensuring the port was free.

3. **Streamlit Console**:
   - Faced challenges in integrating the Ops and Admin consoles with the queue.
   - **Solution**: Fixed by ensuring proper imports and database connections.

4. **Process Management**:
   - Struggled with running producer and consumer simultaneously.
   - **Solution**: Used Supervisor to manage both processes effectively.

---

## What I Learned
1. **Persistent Queues**:
   - Learned how to implement a persistent queue using SQLite.

2. **Producer-Consumer Pattern**:
   - Understood the design and implementation of a producer-consumer system.

3. **Streamlit**:
   - Gained experience in building interactive web-based consoles for monitoring and management.

4. **Supervisor**:
   - Learned how to use Supervisor to manage and monitor multiple processes.

5. **Error Handling**:
   - Improved my skills in debugging and resolving issues related to file paths, ports, and process management.
---
## setbacks or roadblocks Handling
For technical issues (e.g., SQLite errors, Supervisor configuration), I researched online and sought help from ChatGPT.
For design challenges, I revisited the requirements and iterated on the solution.
