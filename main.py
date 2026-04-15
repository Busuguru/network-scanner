import socket
import sys

def scan_ports(target):
    print(f"\nScanning target: {target}")
    print("Scanning ports...\n")

    for port in range(20, 1025):  # scan common ports
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"Port {port}: OPEN")

            sock.close()

        except KeyboardInterrupt:
            print("\nExiting program.")
            sys.exit()

        except socket.gaierror:
            print("Hostname could not be resolved.")
            sys.exit()

        except socket.error:
            print("Couldn't connect to server.")
            sys.exit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <target>")
        sys.exit()

    target = socket.gethostbyname(sys.argv[1])
    scan_ports(target)
