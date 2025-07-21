import psutil


def print_usages():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")

    disk = psutil.disk_usage('/')
    print(f"Disk Usage: {disk.percent}%")

    net = psutil.net_io_counters()
    print(f"Bytes Sent: {net.bytes_sent}, Bytes Received: {net.bytes_recv}")




