import socket

def my_ip_address():

    try:
        # AF_INET - addresses IPv4 , SOCK_DGRAM - UDP protocol
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 8.8.8.8 - google DNS server , 80 port
        s.connect(("8.8.8.8", 80))

        # s.getsockname() - return tuple (IP address, port) , need only IP [0]
        ip = s.getsockname()[0]

        # close connection
        s.close()
        
        print(f'Your IP address : {ip}')
        return ip
        
    except Exception as e:
        print(f'Error : {e}')
        return None

my_ip_address()
