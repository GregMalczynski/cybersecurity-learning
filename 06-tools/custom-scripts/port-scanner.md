# Port Scanner

Port Scanner script detected opened ports and services

## How to execute script

**1. Install Python Environment**
```bash
python -m venv venv
```
**2. Install nmap**
- Install in system ( if U not have nmap : check "nmap --version" )
```bash
sudo apt install nmap
```
- Install nmap module in Python environment venv
```bash
pip install python-nmap
```
- Check installed modules in venv
```bash
pip list | grep nmap
```
**3. Execute script**
```bash
sudo python port-scanner.py <ip address for scan>
```