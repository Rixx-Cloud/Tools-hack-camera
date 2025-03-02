import socket

def check_port_status(host, port):
    """Cek status port (hanya untuk tujuan edukasi)."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        return "Open" if result == 0 else "Closed"
    except Exception as e:
        return f"Error: {e}"

# Contoh penggunaan:
# status = check_port_status("example.com", 80)
# print(status)