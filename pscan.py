import socket
from argparse import ArgumentParser
from datetime import datetime as dt

def tcp_connect_scan(ip):
    try:
        for port in range(1,65535):
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET=IPV4 SOCK_STREAM=TCP
            socket.setdefaulttimeout(1)
            result=s.connect_ex((ip,port))

            if result==0:
                print(f"Port {port} is open")
            s.close()

    except keyboardInterrupt:
        print("\nExiting program")
        sys.exit()
    except socket.gaierror:
        print("Could not resolve hostname")
        sys.exit()
    except socket.error:
        print("could not connect to server, check connection")
        sys.exit()

def main():
    #implementation of argparse for adding flags and parsing args
    parser=ArgumentParser("Usage: python3 pscan.py -H <Target Host or IP>")
    parser.add_argument("-H","--host",action="store",dest="ip",help="target ip or hostname",required=True)
    args=parser.parse_args()

    ip=args.ip
    tcp_connect_scan(ip)

#invoking the main function
if __name__ == "__main__":
    main()
