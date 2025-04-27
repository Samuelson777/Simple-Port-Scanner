# Simple Port Scanner

A simple port scanner written in Python that scans a specified range of ports on a target IP address to determine which ports are open. This project serves as an educational tool for understanding basic networking concepts and ethical hacking practices.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Example](#example)
- [Conclusion](#conclusion)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Features
- Scans a specified range of ports on a target IP address.
- Identifies open and closed ports.
- Displays the time taken for the scan.

## Requirements
- Python 3.x
- Basic knowledge of Python programming

## Example:

- Enter the target IP address: 127.0.0.1
- Enter the starting port number: 1
- Enter the ending port number: 100

View the results in the terminal.

## Example Screenshot

![Simple Port Scanner](https://github.com/user-attachments/assets/e7cce34a-013f-4203-beba-2f4438418de3)

## Conclusion
The Simple Port Scanner project is a foundational exercise in ethical hacking and network security. By creating a Python script that scans a range of ports on a specified IP address, you gain practical experience in socket programming, network protocols, and the basics of penetration testing. This project not only enhances your programming skills but also deepens your understanding of how network services operate and the importance of securing open ports against unauthorized access.

## Future Enhancements
To further develop your skills and improve the functionality of your port scanner, consider implementing the following enhancements:

- **Multi-threading**: Speed up the scanning process by checking multiple ports simultaneously.
- **Protocol Support**: Extend the scanner to support different protocols (e.g., TCP, UDP).
- **Service Detection**: Identify services running on open ports by sending specific requests.
- **Output Options**: Save scan results to a file (e.g., CSV, JSON) for easier analysis.
- **User Interface**: Create a GUI using libraries like Tkinter or PyQt.
- **Network Mapping**: Visualize network topology and identify connected devices.
- **Vulnerability Assessment**: Check for known vulnerabilities associated with services on open ports.
- **Rate Limiting and Throttling**: Implement rate limiting to comply with ethical hacking practices.
- **Logging and Reporting**: Add logging capabilities and generate detailed reports.
- **Integration with Other Tools**: Integrate with security tools or frameworks like Metasploit or Nmap.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
