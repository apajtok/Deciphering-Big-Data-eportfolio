
import psutil
import time
import os

def monitor_process(script_name="parallel_processing.py"):
    """Monitors a Python script for CPU and memory usage."""

    # Find the process ID (PID) of the script
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        if script_name in ' '.join(proc.info['cmdline'] or []):
            pid = proc.info['pid']
            break
    else:
        print(f"Script '{script_name}' not found running.")
        return

    print(f"Monitoring script '{script_name}' (PID: {pid})...")

    try:
        while True:
            process = psutil.Process(pid)
            cpu_percent = process.cpu_percent(interval=1)  # CPU usage over 1 second
            memory_info = process.memory_info()
            memory_percent = process.memory_percent()

            print(f"CPU: {cpu_percent:.1f}%  Memory: {memory_info.rss / (1024 ** 2):.2f} MB ({memory_percent:.1f}%)")

            time.sleep(2)  # Check every 2 seconds

    except psutil.NoSuchProcess:
        print(f"Script '{script_name}' has finished.")

if __name__ == "__main__":
    monitor_process()
