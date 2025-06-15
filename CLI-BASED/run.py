# Import necessary modules from scapy
from scapy.all import sniff, IP, TCP, UDP, Raw, Ether
import os

# --- Configuration ---
# You might need to run this script with elevated privileges (e.g., sudo on Linux,
# Administrator on Windows) to capture packets on network interfaces.

# Define the network interface to sniff on.
# You can find your interface names using commands like 'ipconfig' (Windows),
# 'ifconfig' (Linux/macOS, though 'ip a' is preferred on Linux), or 'netstat -i'.
# Examples: "eth0", "wlan0", "Wi-Fi", "Ethernet"
# Set to None to sniff on all available interfaces (might require more permissions).
NETWORK_INTERFACE = None # Change this to your specific interface, e.g., "eth0" or "Wi-Fi"

# --- Packet Processing Function ---
def packet_callback(packet):
    """
    This function is called for every packet captured.
    It analyzes the packet and prints relevant information.
    """
    print("\n--- New Packet Captured ---")

    # Check for Ethernet Layer (Layer 2)
    if packet.haslayer(Ether):
        eth_layer = packet.getlayer(Ether)
        print(f"  MAC Source: {eth_layer.src}")
        print(f"  MAC Destination: {eth_layer.dst}")
        print(f"  EtherType: {eth_layer.type} (e.g., 0x0800 for IPv4)")

    # Check for IP Layer (Layer 3)
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        print(f"  Source IP: {ip_layer.src}")
        print(f"  Destination IP: {ip_layer.dst}")
        print(f"  Protocol: {ip_layer.proto} ({ip_layer.summary().split()[2]})") # Show protocol number and name

        # Check for TCP Layer (Layer 4 - Transport)
        if packet.haslayer(TCP):
            tcp_layer = packet.getlayer(TCP)
            print(f"    Source Port: {tcp_layer.sport}")
            print(f"    Destination Port: {tcp_layer.dport}")
            print(f"    Flags: {tcp_layer.flags}")
            print(f"    Sequence Number: {tcp_layer.seq}")
            print(f"    Acknowledgement Number: {tcp_layer.ack}")

            # Check for Raw Data (Payload) in TCP
            if packet.haslayer(Raw):
                payload = packet.getlayer(Raw).load
                try:
                    # Attempt to decode as UTF-8, fallback to hexadecimal if not text
                    decoded_payload = payload.decode('utf-8', errors='ignore')
                    print(f"    Payload (TCP): {decoded_payload}")
                except UnicodeDecodeError:
                    print(f"    Payload (TCP) (Hex): {payload.hex()}")

        # Check for UDP Layer (Layer 4 - Transport)
        elif packet.haslayer(UDP):
            udp_layer = packet.getlayer(UDP)
            print(f"    Source Port: {udp_layer.sport}")
            print(f"    Destination Port: {udp_layer.dport}")

            # Check for Raw Data (Payload) in UDP
            if packet.haslayer(Raw):
                payload = packet.getlayer(Raw).load
                try:
                    # Attempt to decode as UTF-8, fallback to hexadecimal if not text
                    decoded_payload = payload.decode('utf-8', errors='ignore')
                    print(f"    Payload (UDP): {decoded_payload}")
                except UnicodeDecodeError:
                    print(f"    Payload (UDP) (Hex): {payload.hex()}")
    else:
        # If no IP layer, just print the packet summary
        print(f"  Packet Summary: {packet.summary()}")

    print("----------------------------")

# --- Main Sniffing Logic ---
def start_sniffer():
    """
    Initializes and starts the network sniffer.
    """
    print("Starting network sniffer...")
    if NETWORK_INTERFACE:
        print(f"Sniffing on interface: {NETWORK_INTERFACE}")
    else:
        print("Sniffing on all available interfaces (may require higher privileges).")
    print("Press Ctrl+C to stop the sniffer.")

    try:
        # Use scapy's sniff function
        # prn: function to apply to each packet
        # store: boolean to store packets or not (False for real-time analysis to save memory)
        # iface: interface to sniff on (optional)
        sniff(prn=packet_callback, store=False, iface=NETWORK_INTERFACE)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Hint: You might need to run this script with administrator/root privileges.")
        print("  On Linux/macOS: sudo python your_script_name.py")
        print("  On Windows: Run your command prompt/PowerShell as Administrator.")
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nSniffer stopped by user.")

# --- Entry Point ---
if __name__ == "__main__":
    # Check if scapy is installed. If not, provide instructions.
    try:
        from scapy.all import sniff
    except ImportError:
        print("Scapy library not found. Please install it using:")
        print("  pip install scapy")
        # On some systems, you might need: pip install scapy[basic] or scapy[complete]
        exit()

    # Clear console for better readability
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/macOS
        os.system('clear')

    start_sniffer()
