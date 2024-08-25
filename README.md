Overview
The Network Packet Sniffer is a Python-based tool that uses the Scapy library to capture and analyze network traffic. It focuses on identifying and displaying information about TCP and UDP packets, including their source and destination IP addresses and ports. This tool is particularly useful for network administrators and security analysts who need to monitor traffic and detect potential security threats in real-time.

Key Features:

Real-time packet capturing and monitoring.
Differentiates and displays TCP, UDP, and other IP packets.
Customizable to monitor specific network interfaces.
Installation
To set up the project on a local machine, follow these steps:

Prerequisites:

Ensure you have Python 3.x installed.
Install Scapy using pip:
pip install scapy
Clone the repository (if hosted on GitHub):
git clone https://https://github.com/Temitayss2/network-packet-sniffer.git
Navigate to the project directory:
cd network-packet-sniffer
Usage
To run the packet sniffer, execute the following command in your terminal:
python sniffer.py
Replace "eth0" with the appropriate network interface for your system (e.g., "wlan0" for wireless connections):
python sniffer.py eth0
The script will start capturing and displaying TCP and UDP packets in real-time.

Example Output:
TCP Packet: 192.168.1.2:50432 -> 192.168.1.1:80
UDP Packet: 192.168.1.2:12345 -> 192.168.1.3:53
Other IP Packet: 192.168.1.4 -> 192.168.1.5
Configuration
To customize the packet sniffer:

Change the network interface: Modify the interface variable in the script to specify which network interface to monitor. For example:
interface = "wlan0"
Adjust packet types: The script is currently configured to detect TCP, UDP, and other IP packets. To extend support to other protocols, update the logic in the packet_callback function.
Customization
To extend the project:

Add more protocols: Modify the packet_callback function to handle additional protocols (e.g., ICMP, HTTP).
Save captured data: Implement functionality to save packet details to a file (e.g., CSV or JSON) for later analysis.
Filter traffic: Add features to filter traffic by IP addresses, ports, or protocols.
Contributing
If you want to contribute to this project, please follow these steps:

Fork the repository on GitHub.
Create a new branch for your feature or bug fix (git checkout -b feature/your-feature).
Commit your changes (git commit -m 'Add new feature').
Push your changes to the branch (git push origin feature/your-feature).
Open a pull request, and describe the changes you made.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions, suggestions, or support, please contact:
Name: [Temitayo Kayode]
Email: [Temitayokayode5@gmail.com]
GitHub: https://github.com/Temitayss2
