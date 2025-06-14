import socket 

def scan_port(target, port): 
    try: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        sock.settimeout(1) 
        result = sock.connect_ex((target, port)) 
        if result == 0:
            print(f"Found open port(s): {port}")
            sock.close()
    except socket.error: print(f"Oops! Couldn't connect to {target}.") 

def scan_target(target):
    print(f"Scanning target {target}...") 
    for port in range(1, 1025): 
        scan_port(target, port)

