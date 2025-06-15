# 🛡️ CLI-Based Real-Time Packet Sniffer

A lightweight, high-performance command-line tool to capture and analyze live network traffic using Python and Scapy. This utility is built for cybersecurity students, network engineers, and penetration testers who want clear visibility into packet-level data directly from the terminal.

🔗 GitHub Repository:
[https://github.com/KIRAN-KUMAR-K3/CodeAlpha\_Basic\_network\_sniffer/tree/main/CLI-BASED](https://github.com/KIRAN-KUMAR-K3/CodeAlpha_Basic_network_sniffer/tree/main/CLI-BASED)

---

## 📌 Project Overview

This CLI-based packet sniffer monitors your network interface and displays detailed information about each captured packet in real time. It extracts and presents key protocol fields including MAC addresses, IP addresses, protocol type, port numbers, TCP flags, sequence/ack numbers, and payloads (when available).

Designed for educational and debugging purposes, it offers a terminal-native alternative to tools like Wireshark, with minimal dependencies and fast setup.

---

## ✨ Features

* ✅ Real-time packet capture and display
* ✅ Parses Ethernet, IP, and TCP headers
* ✅ Highlights source/destination MAC & IP addresses
* ✅ Detects port numbers and TCP control flags
* ✅ Extracts and prints TCP payload (if present)
* ✅ Clean and readable CLI output
* ✅ Uses Scapy — no external PCAP files required

---

## 🖼️ Sample Output

```
--- New Packet Captured ---
  MAC Source: 54:47:e8:b7:73:85
  MAC Destination: 14:13:33:df:6a:0d
  EtherType: 2048 (IPv4)
  Source IP: 157.90.91.74
  Destination IP: 192.168.1.7
  Protocol: 6 (TCP)
    Source Port: 443
    Destination Port: 48036
    Flags: PA
    Sequence Number: 3379048104
    Acknowledgement Number: 410952807
    Payload (TCP): F-{8Mz1.;g5
----------------------------
```

---

## 🛠️ Technologies Used

| Tech         | Purpose                                |
| ------------ | -------------------------------------- |
| Python 3     | Core programming language              |
| Scapy        | Packet capture and protocol parsing    |
| Virtualenv   | Isolated Python environment            |
| Bash (Linux) | For CLI execution with sudo privileges |

---

## 📦 Setup Instructions

Follow the steps below to install and run the packet sniffer:

1️⃣ Clone the Repository:

```bash
git clone https://github.com/KIRAN-KUMAR-K3/CodeAlpha_Basic_network_sniffer.git
cd CodeAlpha_Basic_network_sniffer/CLI-BASED
```

2️⃣ Create and Activate a Virtual Environment:

```bash
python3 -m venv venu
source venu/bin/activate
```

3️⃣ Install Required Packages:

```bash
pip install -r requiremets.txt
```

Note: The spelling of the file is requiremets.txt — ensure that’s used correctly in the command.

4️⃣ Run the Sniffer:

```bash
sudo python3 run.py
```

📌 Important: Root privileges (sudo) are required for Scapy to capture packets from the network interface.

---

## 📁 Project Structure

```
CLI-BASED/
├── requiremets.txt   # Contains Python dependency (scapy)
└── run.py            # Main executable script for packet sniffing
```

---

## 🧠 Use Cases

* 🎓 Ideal for students learning networking & cybersecurity
* 🧪 Network packet inspection for debugging or education
* 🔍 CLI-based alternative to GUI tools like Wireshark
* 🔐 Useful for labs, CTFs, and penetration testing environments

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork this repository
2. Create a new feature branch: git checkout -b feature/your-feature
3. Commit your changes: git commit -m 'Add new feature'
4. Push to the branch: git push origin feature/your-feature
5. Create a Pull Request

Let’s improve this tool together!

---

## 📄 License

This project is licensed under the MIT License.
See the LICENSE file for more information.

---

## 👤 Author

Made with ❤️ by:

* 👨‍💻 Kiran Kumar K
* 🌐 GitHub: @KIRAN-KUMAR-K3
* ✉️ Email: [18kirankumar.k03@gmail.com](mailto:18kirankumar.k03@gmail.com)

---

📢 If you found this project useful, please consider giving it a ⭐ on GitHub!
