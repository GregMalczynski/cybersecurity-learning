# Searching all hosts in isolated network

## Result for :
```bash
nmap -sn -oN reconnaissance.txt 192.168.56.0/24
```
## Founed 4 hosts :

-sn : ping scan
-oN : save scan result to file

Host is up : Active

Low latency: Local Network

1. 192.168.56.1 ( Gateway / Host )
2. 192.168.56.100 ( Virtual Machine / VirtualBox )
2. 192.168.56.101 ( Virtual Machine / VirtualBox )
4. 102.168.56.102 ( Virtual scanning machine )