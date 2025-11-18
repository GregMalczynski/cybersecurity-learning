# Basic scan / vulnerability

## Scan for :
'''bash
nmap -sV -sC -T4 -oN basic-scan.txt 192.168.56.101
'''

## Raport
- Date : **17/11/2025 , 12:30**
- Skaner : **Nmap 7.95**
- Analyst : **Grzegorz Malczynski**

*Basic Data*

- IP: **192.168.56.101**
- Hostname: **metasploitable.localdomain**
- Opened Ports: **23/1000**
- System: **Linux (Debian/Ububtu)**

*Notes*

- MAC : **Oracle VirtualBox** - testing environment
- Workgroup : **Workgroup** - default
- SSL Certificates : **expired 2010**

## Critical Risk

1. Backdoor
```bash
1524/tcp open bindshell Metasploitable root shell
```
- Description: Open backdoor shell with root privilages

2. Backdoor / vsftpd 2.3.4
```bash
21/tcp open ftp vsftpd 2.3.4
```
- Description: backdoor username:) trigger
- AnonymousFTP: enabled ( additional risk )

3. Backdoor / UnrealIRCd
```bash
6667/tcp open irc UnrealIRCd
```
- CVE: CVE-2010-2075

4. Remote Code Execution / Samba 3.0.20
```bash
139/tcp open netbios-ssn Samba smbd 3.0.20-Debian
445/tcp open netbios-ssn Samba smbd 3.0.20-Debian
```
- Description: RCE Username map script
- SMB Signing: Disables ( risk )

## High Risk

1. R-Services
```bash
512/tcp open exec    netkit-rsh rexecd
513/tcp open login   OpenBSD or Solaris rlogind
514/tcp open shell   Netkit rshd
```
- Description: unencrypted outdates protocols
- Risk: plain text data transmission, MITM

2. Telnet
```bash
23/tcp open telnet Linux telnetd
```
- Risk: unencrypted transmission includes passwords

3. Open to the world - PostgreSQL / MySQL
```bash
3306/tcp open mysql      MySQL 5.0.51a-3ubuntu5
5432/tcp open postgresql PostgreSQL DB 8.3.0 - 8.3.7
```
- Risk: Old versions, possibility Brute-Force

4. Network File System - NFS
```bash
2049/tcp open nfs 2-4 (RPC #100003)
```
- Risk: possibility of mounting shares, access to files

5. Without Encryption - VNC
```bash
5900/tcp open vnc VNC (protocol 3.3)
```
- Risk: old protocol, weak authentication

## Medium Risk

1. Outdated Software Versions

- OpenSSH 4.7p1 - should be 9.x +
- Apache 2.2.8 - should be 2.4.x
- BIND 9.4.2 - old DNS version
- Tomcat 5.5 - old version

2. SSLv2 Support
```bash
SSLv2 supported (SMTP, PostgreSQL)
```
- CVE: possibility Brown Attack

3. X11 Server
```bash
6000/tcp open X11 (access denied)
```
- Risk: potential interception of graphics session