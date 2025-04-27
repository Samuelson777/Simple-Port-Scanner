import socket
from datetime import datetime

# Function to scan ports
def scan_ports(target_ip, start_port, end_port):
    print(f"Scanning {target_ip} from port {start_port} to {end_port}")
    # Record the start time
    start_time = datetime.now()

    # Loop through the specified port range
    for port in range(start_port, end_port + 1):
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt
        result = sock.connect_ex((target_ip, port))  # Try to connect to the port

        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")
        sock.close()  # Close the socket

    # Record the end time
    end_time = datetime.now()
    duration = end_time - start_time
    print(f"Scanning completed in: {duration}")

if __name__ == "__main__":
    target = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))
    scan_ports(target, start_port, end_port)