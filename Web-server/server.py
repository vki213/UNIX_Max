import socket 
sock = socket.socket() 
try: 
  sock.bind(('', 80)) 
except OSError: 
  sock.bind(('', 8080)) 
sock.listen(5) 
conn, addr = sock.accept() 
print("Connected", addr) 
conn.close() 
