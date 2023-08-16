import socket
from argparse import ArgumentParser
from datetime import datetime as dt

#implentation of argparse for adding flags and parsing commandline arguments 
parser = ArgumentParser()
parser.add_argument("-H", "--host", action="store", dest="ip")
 
args = parser.parse_args()
ip=args.ip

#formating fix for date and time display
dt_now=dt.now()
dt_format=dt_now.strftime("%m-%d-%Y %H:%M:%S")

#Define target
target=socket.gethostbyname(args.ip) #convert host to ip

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


