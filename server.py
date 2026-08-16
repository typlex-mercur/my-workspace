import http.server
import socketserver
import socket
import webbrowser
import os
import sys

PORT = 8080

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    local_ip = get_local_ip()
    
    server_address = ('0.0.0.0', PORT)
    httpd = socketserver.TCPServer(server_address, CustomHandler)
    
    pc_url = f"http://localhost:{PORT}/index.html"
    mobile_url = f"http://{local_ip}:{PORT}/index.html"
    
    print("=" * 60)
    print(" 🚀 TYPLEX ALL-IN-ONE WORKSPACE SERVER ĐANG CHẠY")
    print("=" * 60)
    print(f" 💻 Máy tính (PC)    : {pc_url}")
    print(f" 📱 Điện thoại (LAN) : {mobile_url}")
    print("=" * 60)
    print(" 👉 Hướng dẫn kết nối điện thoại:")
    print(f" 1. Đảm bảo điện thoại và máy tính kết nối CÙNG mạng Wi-Fi.")
    print(f" 2. Mở trình duyệt trên điện thoại và truy cập: {mobile_url}")
    print(f" 3. Hoặc bấm nút 'Sync' trên PC và quét mã QR để kết nối tức thì.")
    print("=" * 60)
    print(" Nhấn Ctrl + C để dừng server.")
    print("=" * 60)
    
    try:
        webbrowser.open(pc_url)
    except Exception:
        pass
        
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nĐã dừng server.")
        httpd.server_close()

if __name__ == '__main__':
    run()
