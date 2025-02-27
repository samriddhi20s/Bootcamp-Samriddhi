import time

def heartbeat():
    """
    Simulate a heartbeat mechanism to check if a consumer is alive.
    """
    while True:
        print("Heartbeat: Consumer is alive")
        time.sleep(10)  # Send a heartbeat every 10 seconds

def is_timed_out(start_time, timeout=30):
    """
    Check if a process has timed out.
    """
    return time.time() - start_time > timeout