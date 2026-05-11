import socket

def scan_ports(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        s.close()

        if result == 0:
            return True
        else:
            return False
    except Exception:
        return False

def run_scanner():
    print("Port Scanner")
    print("Common Ports: 21(FTP), 22(SSPH), 23(Telnet), 25(SMTP), 53(DNS), 80(HTTP), 110(POP3), 143(IMAP), 443(HTTPS), 3306(MySQL), 3389(RDP)\n")
    target = input("Enter the target IP address/website: ")
    print(f"\nScanning {target} for common ports...\n")
    to_scan = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389, 8080, 8443]
    open_ports = []
    for port in to_scan:
        if scan_ports(target, port):
            print(f"PORT {port} is OPEN")
            open_ports.append(port)
        else:
            print(f"PORT {port} is CLOSED")

if __name__ == "__main__":
    run_scanner()
    again = input("\nScan another? (y/n): ").lower()
    if again == 'y':
        run_scanner()
    else:
        print("Exiting Port Scanner.")