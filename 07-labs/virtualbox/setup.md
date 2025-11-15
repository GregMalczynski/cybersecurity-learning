# My cybersecurity learning / testing lab

## Testing environment

- VirtualBox : isolated virtual network
- Kali-Linux : (102.168.56.101) - attacker
- Metasploitable2 : (192.168.56.100) - target

## Network configuration

- Type : Internal Network
- Scope : '192.168.56.0/24'

## Verify

```bash
ping 192.168.56.101
nmap 192.168.56.101