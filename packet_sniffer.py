from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        if TCP in packet:
            tcp_src_port = packet[TCP].sport
            tcp_dst_port = packet[TCP].dport
            print(f"TCP Packet: {ip_src}:{tcp_src_port} -> {ip_dst}:{tcp_dst_port}")

        elif UDP in packet:
            udp_src_port = packet[UDP].sport
            udp_dst_port = packet[UDP].dport
            print(f"UDP Packet: {ip_src}:{udp_src_port} -> {ip_dst}:{udp_dst_port}")

        else:
            print(f"Other IP Packet: {ip_src} -> {ip_dst}")

def start_sniffing(interface):
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    interface = "eth0"  # Replace with the correct interface, e.g., "eth0", "wlan0", etc.
    start_sniffing(interface)
