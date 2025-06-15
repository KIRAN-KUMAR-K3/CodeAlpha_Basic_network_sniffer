Simulated Network Sniffer
🚀 Project Overview
The Simulated Network Sniffer is a web-based application designed to help users understand the fundamental concepts of network packet capture, analysis, and data flow in a user-friendly graphical interface. Unlike traditional network sniffers that require complex setups and elevated system privileges to capture live traffic, this project simulates the process by leveraging the power of a Large Language Model (LLM) to generate realistic-looking packet data.

This tool is perfect for:

Learning Network Basics: Visualize the structure and content of network packets.

Understanding Protocols: Observe simulated data flowing through various common network protocols (TCP, UDP, ICMP, ARP).

Interactive Exploration: Click and expand packets to examine detailed information like source/destination IPs, ports, flags, and payloads.

✨ Features
Web-Based GUI: Accessible directly in any modern web browser, no complex installations required.

Simulated Packet Generation: Uses the Google Gemini API to generate diverse and realistic network packet data on demand.

Detailed Packet Analysis: Displays crucial information for each packet, including:

MAC Source/Destination

IP Source/Destination

Protocol (TCP, UDP, ICMP, ARP)

Source/Destination Ports

TCP Flags (for TCP packets)

Sequence and Acknowledgement Numbers (for TCP packets)

Simulated Payloads (with indication for encrypted/unreadable data)

Responsive Design: Optimized for viewing and interaction on various devices, from mobile phones to desktop computers.

Accordion View: Clean and organized display of packet details, allowing users to expand and collapse information for better readability.

🛠️ Technologies Used
HTML5: The foundational markup language for structuring the web page.

React (via CDN): A JavaScript library for building user interfaces, used for creating interactive components.

Tailwind CSS (via CDN): A utility-first CSS framework for rapid and responsive styling.

Google Gemini API: Utilized to generate the simulated network packet data.

Babel (via CDN): Used to transpile JSX syntax in the browser for single-file execution.

🚦 Getting Started
To run this project, you only need a web browser and your Google Gemini API key.

Prerequisites
Web Browser: Any modern web browser (Chrome, Firefox, Edge, Safari, etc.).

Google Gemini API Key: You will need an API key from Google AI Studio to fetch simulated packet data.

Go to Google AI Studio.

Sign in with your Google account.

Navigate to the "API keys" section (usually on the left sidebar).

Generate a new API key if you don't have one. Keep this key confidential!

Installation and Setup
Clone the Repository:

git clone https://github.com/KIRAN-KUMAR-K3/CodeAlpha_Basic_network_sniffer.git
cd CodeAlpha_Basic_network_sniffer

Locate index.html:
The entire application is self-contained within the index.html file in the root of the repository.

Insert Your Gemini API Key:

Open the index.html file in a text editor (like VS Code, Notepad++, Sublime Text, etc.).

Search for the line:

const apiKey = "YOUR_GEMINI_API_KEY_HERE";

Replace "YOUR_GEMINI_API_KEY_HERE" with your actual Gemini API key that you obtained in the prerequisites step.

Save the index.html file.

Running the Application
After inserting your API key and saving the file:

Simply open the index.html file in your web browser. You can do this by double-clicking the file in your file explorer.

The application will load, and you can start simulating network sniffing!

💡 Usage
"Simulate Sniffing" Button: Click this button to request the LLM to generate a new set of simulated network packets. The previous packets will be cleared.

"Clear Packets" Button: Click this button to remove all currently displayed packets.

Inspect Packets: Each captured packet is displayed as a card. Click on a packet card's header to expand or collapse its detailed information.

🤝 Contributing
Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes.

Commit your changes (git commit -m 'feat: Add new feature').

Push to the branch (git push origin feature/your-feature-name).

Open a Pull Request.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

📧 Contact
If you have any questions or feedback, feel free to reach out:

KIRAN KUMAR K - Your GitHub Profile
