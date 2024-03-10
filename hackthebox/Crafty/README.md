# Crafty

## Scanning 
- Using nmap tools: `nmap -sV -A -p- --min-rate=1000 10.10.11.249 -v -oN ~/nmap/crafty`
```shell
<result>
┌──(toan㉿kali)-[~/note_hackthebox_cryptohack_ctf/hackthebox]
└─$ cat ~/nmap/crafty                                                       
# Nmap 7.94SVN scan initiated Sun Mar 10 05:03:59 2024 as: nmap -sV -A -p- --min-rate=1000 -v -oN /home/toan/nmap/crafty 10.10.11.249
Nmap scan report for 10.10.11.249
Host is up (0.25s latency).
Not shown: 65533 filtered tcp ports (no-response)
PORT      STATE SERVICE   VERSION
80/tcp    open  http      Microsoft IIS httpd 10.0
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Did not follow redirect to http://crafty.htb
|_http-server-header: Microsoft-IIS/10.0
25565/tcp open  minecraft Minecraft 1.16.5 (Protocol: 127, Message: Crafty Server, Users: 0/100)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Mar 10 05:06:31 2024 -- 1 IP address (1 host up) scanned in 151.93 seconds
                  

```
- Port is opened: 80 (webservice), 25565.
- When you go to http://<target_host>, it redirected to other domain. *crafty.htb*
![image 1](./image/img1)
