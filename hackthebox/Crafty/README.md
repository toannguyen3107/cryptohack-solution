# Crafty - Write-up

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
- add domain into **/etc/hosts**. `echo "10.10.11.249 crafty.htb" | sudo tee -a /etc/hosts`.
 
Again, goto web -> login success!
![image 2](./image/img2)

You see in the main page, it recommend redirect to `play.crafty.htb`, same as the last step add this domain into /etc/host, and go to play.crafty.htb.

- Next, you need to install minecraft client in your linux machine, it use to connect the target server. You can search internet to install!

## Exploit
- Use log4shell, pyCraft -> msfvenom create payload
- decode java program (program java in plugins folder at server is accessed) with jadx (clone and install from github) -> see password for administrator
- using runas program (clone it from github), tranfer it to server, runas adminstrator account with other payload. -> access with privilege's administrator. 
### End, Thanks for read 
## ***Some screen window is useful for you!***
![img 3](./image/img3)
![img 4](./image/img4)
![img 5](./image/img5)
![img 6](./image/img6)
![img 7](./image/img7)
