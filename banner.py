import socket

def grab_banner(ip, port):
    try:
        # Create TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)

        # Connect to target
        s.connect((ip, port))

        # Send simple request
        s.send(b"Hello\r\n")

        # Receive banner
        banner = s.recv(1024)

        if banner:
            print("Banner received:")
            print(banner.decode(errors="ignore"))
        else:
            print("No banner received.")

        s.close()

    except Exception as e:
        print("Error:", e)


# Take input from user
ip = input("Enter target IP: ")
port = int(input("Enter target port: "))

grab_banner(ip, port)
