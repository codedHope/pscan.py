import sys
import socket
from datetime import datetime as dt

#formating fix for date and time display
dt_now = dt.now()
dt_format = dt_now.strftime("%m/%d/%Y %H:%M:%S")

#Define target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #convert host to ip
else:
    sys.stderr.write(f"Usage: {sys.argv[0]} <ip>\n")
    sys.exit()

#banner
print(f"\nStarting scanner.py at {dt_format}")
print(f"Scan report for ({target})\n")

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=s.connect_ex((target,port))
        
        if result==0:
            print(f"Port {port} is open")
        s.close()

except keyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to server")
    sys.exit()
