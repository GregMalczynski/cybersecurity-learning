import sys
import nmap

def scan_host(target_ip):
    print(f'*** Scanner ports and services ***')
    print(f'\nScan Start IP : {target_ip}')
    print('-' * 30)

    nm = nmap.PortScanner()

    try:

        nm.scan(target_ip, arguments="-sS -sV -p 1-1000")

        for host in nm.all_hosts():
            print(f'\n[+] Host: {host}')
            print(f'[+] Status: {nm[host].state()}')

            for protocol in nm[host].all_protocols():
                print(f'\n[+] Protocol: {protocol}')

                ports = nm[host][protocol].keys()
                for port in sorted(ports):
                    state = nm[host][protocol][port]['state']
                    service = nm[host][protocol][port]['name']
                    version = nm[host][protocol][port].get('version', '')

                    print(f'  Port : {port}: {state} | {service} {version}')
    
    except Exception as e:
        print(f'Error : {e}')
        sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(f'Used: {sys.argv[0]} <target_ip>')
        sys.exit(1)

    target = sys.argv[1]
    scan_host(target)