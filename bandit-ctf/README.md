---
title: WARGAME BANDIT - OVERTHEWIRE
date: 2024-01-26 21:03:20
tags: ['wargame', 'bandit', 'overthewire']
---
[Bandit](https://overthewire.org/wargames/bandit/bandit0.html)

# Lever 0
## level goad
The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.
## Solution
 - step 1:
```shell
ssh bandit0@bandit.labs.overthewire.org -p 2220
```
 - step 2:

 - Enter password: bandit0

{% asset_img bandit1.png enter password %}
## Result
```shell
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
bandit0@bandit:~$ 
```


# Level 1 -> 2
## Level Goal

The password for the next level is stored in a file called - located in the home directory.
## Solution

 - Step 1: Log in to bandit1 using the password found in bandit0.
 - Step 2: You'll see a '-' file on the screen if you use the 'ls' command. Read it.
 
 ```shell
 bandit1@bandit:~$ ls
-
bandit1@bandit:~$ file ./-
./-: ASCII text
bandit1@bandit:~$ cat ./-
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
bandit1@bandit:~$ 
 ```


# Level 2 -> 3
## Level Goal

The password for the next level is stored in a file called spaces in this filename located in the home directory
## Solution

 - Step 1: Log in to bandit2.
 - Use the ls command to view the file named 'spaces in this filename', then read it.
 ## Result

 ```shell
  bandit2@bandit:~$ file spaces\ in\ this\ filename 
  spaces in this filename: ASCII text
  bandit2@bandit:~$ cat spaces\ in\ this\ filename 
  aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
  bandit2@bandit:~$ 
 ```


# Level 3 -> 4
## Level Goal

The password for the next level is stored in a hidden file in the inhere directory.
## Solution 

- You need to access the target machine.
```shell
ssh bandit3@bandit.labs.overthewire.org -p 2220
```
- Analyze the folder, check for folders or files within it. If you only use the ls command, you won't see anything. Now, using ls -a (all option), you'll see the file .hidden; this is the target file. Read it. Read [ls's manual](https://www.man7.org/linux/man-pages/man1/ls.1.html) if you like!
{%asset_img bandit2.png result3to4%}
## Result

```shell
bandit3@bandit:~$ cat inhere/.hidden
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
```


# Level 4 -> 5
## Level Goal
The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

## Solution
- Access the target machine.
- In this challenge, you need to file what file `human-readable`. How to find it? The human-readable file is file human can read it. It include ASCII. i use `file` command.
```shell
cd inhere
file ./-file*
```
{%asset_img bandit3.png bandit4to5%}

## Result
`lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR`

# Level 5 -> 6
## Level Goal
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
1. human-readable
2. 1033 bytes in size
3. not executable

## Solution 
- Using `find` command. Read manual `man find` or [man find](https://man7.org/linux/man-pages/man1/find.1.html), you see 1033 bytes (-size 1033c) and not executable (\! -executable) and type is the file (-type f). You can check file result, it is a human-readable.

```shell
cd inhere
find . -type f \! -executable -size 1033c
```
{%asset_img bandit4.png bandit5to6%}

## Result
`P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU`


# Level 6 -> 7
## Level Goal
The password for the next level is stored somewhere on the server and has all of the following properties:
1. owned by user bandit7
2. owned by group bandit6
3. 33 bytes in size

## Solution
- 33 bytes in size(-size 33c), user bandit7 (-user bandit7), group bandit6 (-group bandit6).
- Santisize the error with 2>/dev/null
- you can read [permission file on linux](https://linuxhandbook.com/linux-file-permissions/) if you like!
```shell
find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null
```
{%asset_img bandit5.png bandit 6 to 7 %}

## Result
`z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S`

# Level 7 -> 8
## Level Goal
The password for the next level is stored in the file data.txt next to the word `millionth`

## Solution 
- This is a large file. Using wc -l data.txt, data.txt contains 98,567 lines.
- First, I used the grep command with the keyword "millionth." Yes, it's correct. I found the target code.

{%asset_img bandit6.png bandit 7 to 8%}

## Result
`TESKZC0XvTetK0S9xNwm25STk5iWrBvP`


# Level 8 -> 9
## Level Goal
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

# Solution
- Same as level 7, but this time you don't have a keyword. However, the question provides a hint: `only once.`
- Refer to the sort and uniq manuals: [manual's sort](https://www.man7.org/linux/man-pages/man1/sort.1.html) and [manual's uniq](https://man7.org/linux/man-pages/man1/uniq.1.html)

```shell
sort data.txt | uniq -u
```
{%asset_img bandit7.png Bandit 8 to 9%}

## Result
`EN632PlfYiZbn3PhVK3XOGSlNInNE00t`

# Level 9 -> 10
## Level Goal
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters

## Solution
- Using the `strings` command is helpful; it filters and provides strings that humans can read. After that, you can use the `grep` command to further filter using several '=' characters
```shell
strings data.txt | grep -- '==='
```
{%asset_img bandit8.png Bandit 9 to 10%}
## Result
`G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s`

# Level 10 -> 11
## Level Goal
The password for the next level is stored in the file data.txt, which contains base64 encoded data

## Solution
- using `base64` command. See command `base64 --help`
```shell
base64 -d < data.txt
```
{%asset_img bandit9.png Bandit 10 to 11%}

## Result
`6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM`

# Level 11 -> 12
## Level Goal
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

## Solution
- using `tr` command, see at `tr --help` or `man tr`.
```shell
tr [a-zA-Z] [n-za-mN-ZA-M] < data.txt
```
{%asset_img bandit10.png Bandit 10 to 11%}

## Result
`JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv`

# Level 12 -> 13
## Level Goal
&emsp;The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

## Solution
- Login bandit12.
```shell
ssh bandit12@<host> -p 2220
```
- Go to the tmp folder and create a new folder. Navigate to the new folder, then copy the file data from the Home folder and paste it here.
```shell
cd /tmp
mktemp -d
<output folder>
cd <output folder>
cp ~/data.txt .
```
- I use `xxd` command to see, [read if you like](https://linuxhandbook.com/xxd-command/) and [manual's xxd](https://linux.die.net/man/1/xxd). I use `-r` option that revert hexdump to binary... (read manual).
```shell
xxd -r data.txt output
```
{%asset_img bandit11.png BanditLevel12%}
- Next, check file type (`file` command).
```shell
file output
output: gzip compressed data......
```
- Uncompress and repeat the process until you see the target file.
```shell
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ mv output output.gz
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ gzip -d output.gz
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ ls
data.txt  output
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ file output
output: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ mv output output.bz2
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ bzip2 -d output.bz2
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ file output
output: gzip compressed data, was "data4.bin", last modified: Thu Oct  5 06:19:20 2023, max compression, from Unix, original size modulo 2^32 20480
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ mv output output.gz
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ gzip -d output.gz
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ ls
data.txt  output
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ file output
output: POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ mv output output.tar
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ tar -xvf output.tar
data5.bin
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ file data5.bin
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ mv data5.bin data.tar
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ tar -xvf data.tar
data6.bin
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ file data6.bin
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ mv data.gz2 data.bz2
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ bzip2 -d data.bz2
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ file data
data: POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ mv data data.tar
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ tar -xvf data.tar
data8.bin
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ file data8.bin
data8.bin: gzip compressed data, was "data9.bin", last modified: Thu Oct  5 06:19:20 2023, max compression, from Unix, original size modulo 2^32 49
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ mv data8.bin data.gz
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ gzip -d data.gz
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ file data
data: ASCII text
bandit12@bandit:/tmp/tmp.ylM3UOLSpW$ cat data
The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
```

## Result 
`wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw`


# Level 13 -> 14
## Level Goal
The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on

## Solution
The password is located at /etc/bandit_pass/bandit14, but it can only be read by bandit14. We need to log in as bandit14. Check the home folder; you'll find sshkey.private there. This file is used for authentication by bandit14. Refer to the [SSH manual](https://www.man7.org/linux/man-pages/man1/ssh.1.html). Look for the -i option and use it. (Note: port 2220)
```shell
ssh -i sshkey.private bandit14@localhost  -p 2220
```
&emsp;You logon as bandit14, read password!.

## Result
`fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq`

# Level 14 -> 15
## Level Goal
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

## Solution
&emsp;Connect to localhost on port 30000 and submit the password using the `nc` or `telnet` command.
```shell
nc localhost 30000
<paste password level 14 in this>
``` 
{%asset_img bandit12.png BanditLevel12%}

## Result
`jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt`

# Level 15 -> 16
## Level Goal
&emsp;The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.
&emsp;Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…
## Solution
&emsp;You can do it from the hint above
```shell
bandit15@bandit:~$ openssl s_client -connect localhost:30001 -ign_eof 
Can't use SSL_get_servername
... (skip message retn)
---
read R BLOCK
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
Correct!
JQttfApK4SeyHwDlI9SXGR50qclOAil1

closed
bandit15@bandit:~$
```
## Result
`JQttfApK4SeyHwDlI9SXGR50qclOAil1`

# Level 16 -> 17
## Level Goal


# Solution
&emsp;First, we need to scan port range 31000 - 32000. Using `nmap` tool for this purpose.
```shell
bandit16@bandit:~$ nmap -p31000-32000 -T3 -v localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2024-01-30 13:41 UTC
Initiating Ping Scan at 13:41
Scanning localhost (127.0.0.1) [2 ports]
Completed Ping Scan at 13:41, 0.00s elapsed (1 total hosts)
Initiating Connect Scan at 13:41
Scanning localhost (127.0.0.1) [1001 ports]
Discovered open port 31960/tcp on 127.0.0.1
Discovered open port 31046/tcp on 127.0.0.1
Discovered open port 31691/tcp on 127.0.0.1
Discovered open port 31790/tcp on 127.0.0.1
Discovered open port 31518/tcp on 127.0.0.1
Completed Connect Scan at 13:41, 0.02s elapsed (1001 total ports)
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00011s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 0.06 seconds
```
&emsp;You can see that 5 ports are opened. it include: 31046, 31518, 31691, 31790. Scanning the services on some ports still uses `nmap` tool.
```shell
bandit16@bandit:~$  nmap -p31046,31518,31790,31960 -A -sV localhost -v -T3
Starting Nmap 7.80 ( https://nmap.org ) at 2024-01-30 13:46 UTC
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 13:46
Completed NSE at 13:46, 0.00s elapsed
Initiating NSE at 13:46
Completed NSE at 13:46, 0.00s elapsed
Initiating NSE at 13:46
Completed NSE at 13:46, 0.00s elapsed
Initiating Ping Scan at 13:46
Scanning localhost (127.0.0.1) [2 ports]
Completed Ping Scan at 13:46, 0.00s elapsed (1 total hosts)
Initiating Connect Scan at 13:46
Scanning localhost (127.0.0.1) [4 ports]
Discovered open port 31790/tcp on 127.0.0.1
Discovered open port 31518/tcp on 127.0.0.1
Discovered open port 31960/tcp on 127.0.0.1
Discovered open port 31046/tcp on 127.0.0.1
Completed Connect Scan at 13:46, 0.00s elapsed (4 total ports)
Initiating Service scan at 13:46
Scanning 4 services on localhost (127.0.0.1)
Service scan Timing: About 25.00% done; ETC: 13:49 (0:02:06 remaining)
Completed Service scan at 13:48, 98.13s elapsed (4 services on 1 host)
NSE: Script scanning 127.0.0.1.
Initiating NSE at 13:48
Completed NSE at 13:48, 0.05s elapsed
Initiating NSE at 13:48
Completed NSE at 13:48, 0.10s elapsed
Initiating NSE at 13:48
Completed NSE at 13:48, 0.00s elapsed
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00091s latency).

PORT      STATE SERVICE     VERSION
31046/tcp open  echo
31518/tcp open  ssl/echo
| ssl-cert: Subject: commonName=localhost
| Subject Alternative Name: DNS:localhost
| Issuer: commonName=localhost
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2024-01-27T16:43:15
| Not valid after:  2024-01-27T16:44:15
| MD5:   e73b dea0 7e46 7f63 c084 fcbd 0a86 8be2
|_SHA-1: 3c5d 9fb0 2daa 9bca b871 d718 8378 aef4 4780 5e53
31790/tcp open  ssl/unknown
| fingerprint-strings:
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq, TerminalServerCookie:
|_    Wrong! Please enter the correct current password
| ssl-cert: Subject: commonName=localhost
| Subject Alternative Name: DNS:localhost
| Issuer: commonName=localhost
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2024-01-27T16:43:16
| Not valid after:  2024-01-27T16:44:16
| MD5:   6de1 2b79 fb4e 3129 44c5 f8a4 bae6 0948
|_SHA-1: ae07 caca 9d09 48d4 320e a207 5b82 4872 690e c920
31960/tcp open  echo
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port31790-TCP:V=7.80%T=SSL%I=7%D=1/30%Time=65B8FDD4%P=x86_64-pc-linux-g
...
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 98.87 seconds
```
&emsp;From the message retn, you can guess the port vuln. Look at 31790 you see `Wrong! Please enter the correct current password`. Yah, i think this port will give the key. Similar as the last level. Using `openssl s_client`.
```shell
openssl s_client -connect localhost:31790 -ign_eof
<Paste this level password>
```
{%asset_img bandit13.png Result level 16%}
## Result
&emsp;*Save this, it will use for the next level*
```shell
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

```

# Level 17 -> 18
## Level Goal
There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

## Solution
&emsp;Using the key at the last level, save it in a file, and set permissions for it.(`chmod 700 <filename>`)!
{%asset_img bandit14.png bandit14%}
&emsp;Connect with bandit17 account uses the key above. `ssh -i key bandit17@bandit.labs.overthewire.org -p 2220`
&emsp;Using the `ls` command, you can see two files: `password.new` and `password.old`. We will use the `diff` command to compare the two files and find the differences.
```shell
bandit17@bandit:~$ diff passwords.old passwords.new
42c42
< p6ggwdNHncnmCNxuAt0KtKVq185ZU7AW
---
> hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg
```
## Result

`hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg`

# Level 18 -> 19
## Level Goal
The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

## Solution
&emsp;When you log in bandit18, it shows more info. From this info, i guess that we need to add code when connecting. 
`ssh ... <command>`
```shell
┌[parrot]─[08:06-31/01]─[/home/parrot]
└╼parrot$ssh bandit18@bandit.labs.overthewire.org -p 2220 "ls" 
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 
readme
```
&emsp;It correct! read `readme` file!
```shell
┌[parrot]─[08:07-31/01]─[/home/parrot]
└╼parrot$ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat ~/readme"
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 
awhqfNnAbc1naukrpqDYcF95h7HoMTrC
```
- Alternatively, you could use flag `-t` in ssh command spawn shell. `ssh....... -t /bin/sh`.
## Result
`awhqfNnAbc1naukrpqDYcF95h7HoMTrC`

# Level 19 -> 20
## Level Goal
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

## Solution
&emsp;The file name `bandit20-do` indicates that this program wil run command as the bandit20 user.
{%asset_img bandit15.png bandit15%}

## Result
`VxCazJaVykI6W36BkBU0mJTCM8rR95XT`


# Level 20 - 21
## Level Goal
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

## Solution
&emsp;First, create a simple TCP server. I choose to have it listen on port 4444. Run it in a session.`&`. 
```shell
bandit20@bandit:~$  echo -n "VxCazJaVykI6W36BkBU0mJTCM8rR95XT" | nc -lp 4444  &
[1] 134621
bandit20@bandit:~$ ./suconnect 4444
Read: VxCazJaVykI6W36BkBU0mJTCM8rR95XT
Password matches, sending next password
NvEJF7oVjkddltPSrdKEFOllh9V1IBcq
```
{%asset_img bandit16.png bandit16%}
## Result
`NvEJF7oVjkddltPSrdKEFOllh9V1IBcq`

# Level 21 - 22
## Level Goal
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

## Solution
&emsp;You can read [`cron` manual](https://www.man7.org/linux/man-pages/man8/cron.8.html). 
&emsp;First, you need to check the `/etc/cron.d/` folder. You will find a file named `cronjob_bandit22`. Check this file to see that it automatically runs the file `/usr/bin/cronjob_bandit22.sh`. Read this file to retrieve the key.
```shell
bandit21@bandit:~$ cat /etc/cron.d/cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null

bandit21@bandit:~$ cat /usr/bin/cronjob_bandit22.sh
...
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fg
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

bandit21@bandit:~$ cd /tmp/
bandit21@bandit:/tmp$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff
```

## Result
`WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff`

# Level 22 -> 23
## Level Goal
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

## Solution
&emsp;Check cron job. Read `cronjob_bandit23`. When reboot it run command `/usr/bin/cronjob_bandit23.sh`. Read clearly that file.
```shell
bandit22@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit23.sh
...
myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"
cat /etc/bandit_pass/$myname > /tmp/$mytarget
```
&emsp;We need write a program to reverse it because this cronjob run as bandit23 => `myname=bandit23`. We have:  
```shell
cd /tmp
nano shell
<....>
#!/bin/bash

myname=bandit23
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

cat /tmp/$mytarget
<Ctrl + x>
chmod +x shell
./shell
QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G
```

## Result
`QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G`


# Level 23 -> 24
## Level Goal 
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

## Solution
{%asset_img bandit17.png bandit17%}
&emsp;Create folder in /tmp folder. Set permission all for this. create `shell.sh`. we have `shell.sh`.
```shell
#!/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/tmp.MJFUqp7VWR/password
```
&emsp;Copy `shell.sh` and paste it into `/var/spool/bandit24/foo` with the name `shell.sh` because when checking the crontab, it shows that it runs `/usr/bin/cronjob_bandit24.sh`.
```shell
bandit23@bandit:/tmp/tmp.MJFUqp7VWR$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done

bandit23@bandit:/tmp/tmp.MJFUqp7VWR$ 
```

## Result
`VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar`

# Level 24 -> 25
## Level Goal
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
You do not need to create new connections each time

## Solution
&emsp;The process to solve this level is a waste of time! you create a foldeer in `/tmp` (`mktemp -d`) and write a shell code file following the instructions below.
```shell
bandit24@bandit:~$ cd $(mktemp -d)
bandit24@bandit:/tmp/tmp.6SBIsxKjSZ$ nano shell.sh
Unable to create directory /home/bandit24/.local/share/nano/: No such file or directory
It is required for saving/loading search history or cursor positions.

bandit24@bandit:/tmp/tmp.6SBIsxKjSZ$ chmod +x shell.sh 
bandit24@bandit:/tmp/tmp.6SBIsxKjSZ$ ./shell.sh 
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Correct!
The password of user bandit25 is p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d

Exiting.
bandit24@bandit:/tmp/tmp.6SBIsxKjSZ$ cat shell.sh 
#!/bin/bash
for i in {0000..9999}
do 
echo "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $i"
done | nc localhost 30002 | grep -v Wrong
```

## Result
`p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d`

# Level 25 -> 26
## Level Goal
Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

## Solution
&emsp; You private key connect ssh. Bandit26 will run program before you login. what program?
```shell
bandit25@bandit:~$ ls
bandit26.sshkey
bandit25@bandit:~$ cat /etc/passwd | grep bandit26
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
bandit25@bandit:~$ ls
bandit26.sshkey
bandit25@bandit:~$ cat /usr/bin/showtext 
#!/bin/sh

export TERM=linux

exec more ~/text.txt
exit 0
bandit25@bandit:~$ 
```
&emsp;Yes, we found the program. How to find key? you need to `diminish` window terminal following the vertical side. 
`bandit25@bandit26:~$ ssh -i bandit26.sshkey bandit26@localhost -p 2220`
&emsp;After the type `v` in keyboard (This act will call vim program), if you want to know how to it, read `showtext`'s manual. You can see vim program run. Type `ESC` after that type `:e /etc/bandit_pass/bandit26`  (:e\[dit\] file - edit a file in a new buffer).
## Result
`c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1`

# Level 26 -> 27
## Level Goal
Good job getting a shell! Now hurry and grab the password for bandit27!

## Solution
&emsp;Follow the Bandit level 25 to 26 walkthrough until the Vim program appears. Type `Esc`, then `:set shell=/bin/bash`, followed by Esc again and `:shell`. This will bring up Bandit26
```shell
bandit26@bandit:~$ ls
bandit27-do  text.txt
bandit26@bandit:~$ file bandit27-do 
bandit27-do: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=037b97b430734c79085a8720c90070e346ca378e, for GNU/Linux 3.2.0, not stripped
bandit26@bandit:~$ ./bandit27-do 
Run a command as another user.
  Example: ./bandit27-do id
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS
bandit26@bandit:~$ 
```

## Result
`YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS`

# Level 27 -> 28
## Level Goal
There is a git repository at ssh://bandit27-git@localhost/home/bandit27-git/repo via the port 2220. The password for the user bandit27-git is the same as for the user bandit27.
Clone the repository and find the password for the next level.

## Solution
&emsp;Create folder in /tmp, `cd $(mktemp -d)` Note: when git clone the host is `localhost:2220`.
```shell
bandit27@bandit:/tmp/tmp.IkSs9HdrbP$ git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit27/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit27-git@localhost's password: 
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
bandit27@bandit:/tmp/tmp.IkSs9HdrbP$ ls
repo
bandit27@bandit:/tmp/tmp.IkSs9HdrbP$ cd repo/
bandit27@bandit:/tmp/tmp.IkSs9HdrbP/repo$ ls
README
bandit27@bandit:/tmp/tmp.IkSs9HdrbP/repo$ cat README 
The password to the next level is: AVanL161y9rsbcJIsFHuw35rjaOM19nR
bandit27@bandit:/tmp/tmp.IkSs9HdrbP/repo$ 

```

## Result
`AVanL161y9rsbcJIsFHuw35rjaOM19nR`

# Level 28 -> 29
## Level Goal
There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo via the port 2220. The password for the user bandit28-git is the same as for the user bandit28.

## Solution
```shell
bandit28@bandit:~$ cd $(mktemp -d)
bandit28@bandit:/tmp/tmp.iI1qKCIpO8$ git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yees
Please type 'yes', 'no' or the fingerprint: yes
Could not create directory '/home/bandit28/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit28/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit28-git@localhost's password: 
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 9 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (9/9), done.
Resolving deltas: 100% (2/2), done.
bandit28@bandit:/tmp/tmp.iI1qKCIpO8$ ls
repo
bandit28@bandit:/tmp/tmp.iI1qKCIpO8$ cd repo/
bandit28@bandit:/tmp/tmp.iI1qKCIpO8/repo$ ls
README.md
bandit28@bandit:/tmp/tmp.iI1qKCIpO8/repo$ cat README.md 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx

bandit28@bandit:/tmp/tmp.iI1qKCIpO8/repo$ git log
commit 14f754b3ba6531a2b89df6ccae6446e8969a41f3 (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Thu Oct 5 06:19:41 2023 +0000

    fix info leak

commit f08b9cc63fa1a4602fb065257633c2dae6e5651b
Author: Morla Porla <morla@overthewire.org>
Date:   Thu Oct 5 06:19:41 2023 +0000

    add missing data

commit a645bcc508c63f081234911d2f631f87cf469258
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Oct 5 06:19:41 2023 +0000

    initial commit of README.md

bandit28@bandit:/tmp/tmp.iI1qKCIpO8/repo$ git checkout f08b9c
Previous HEAD position was a645bcc initial commit of README.md
HEAD is now at f08b9cc add missing data
bandit28@bandit:/tmp/tmp.iI1qKCIpO8/repo$ cat README.md 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S

bandit28@bandit:/tmp/tmp.iI1qKCIpO8/repo$ 
```
- Check git log and get pass!
## Result 
`tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S`

# Level 29 - 30
## Level Goal
There is a git repository at ssh://bandit29-git@localhost/home/bandit29-git/repo via the port 2220. The password for the user bandit29-git is the same as for the user bandit29.

## Solution
&emsp;Do the same with the last level, and check the other branches on git.
```shell
bandit29@bandit:/tmp/tmp.16Vf1n7Hq2/repo$ git branch -a
* (HEAD detached at fca34dd)
  master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
bandit29@bandit:/tmp/tmp.16Vf1n7Hq2/repo$ git checkout dev
Previous HEAD position was fca34dd initial commit of README.md
Branch 'dev' set up to track remote branch 'dev' from 'origin'.
Switched to a new branch 'dev'
bandit29@bandit:/tmp/tmp.16Vf1n7Hq2/repo$ ls
code  README.md
bandit29@bandit:/tmp/tmp.16Vf1n7Hq2/repo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS

bandit29@bandit:/tmp/tmp.16Vf1n7Hq2/repo$ 

```

## Result
`xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS`

# Level 30 -> 31
## Level Goal
There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo via the port 2220. The password for the user bandit30-git is the same as for the user bandit30.

## Solution
```shell
bandit30@bandit:/tmp/tmp.SrNnZTB0RH/repo$ git log -a
commit d39631d73f786269b895ae9a7b14760cbf40a99f (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Oct 5 06:19:45 2023 +0000

    initial commit of README.md
bandit30@bandit:/tmp/tmp.SrNnZTB0RH/repo$ git branch -v
* master d39631d initial commit of README.md
bandit30@bandit:/tmp/tmp.SrNnZTB0RH/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
bandit30@bandit:/tmp/tmp.SrNnZTB0RH/repo$ git remote -v
origin	ssh://bandit30-git@localhost:2220/home/bandit30-git/repo (fetch)
origin	ssh://bandit30-git@localhost:2220/home/bandit30-git/repo (push)
bandit30@bandit:/tmp/tmp.SrNnZTB0RH/repo$ git tag
secret
bandit30@bandit:/tmp/tmp.SrNnZTB0RH/repo$ git show secret 
OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt
bandit30@bandit:/tmp/tmp.SrNnZTB0RH/repo$ 
```
[read about git tag](https://stackoverflow.com/questions/35979642/what-is-git-tag-how-to-create-tags-how-to-checkout-git-remote-tags)

## Result
`OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt`


# Level 31 -> 32
## Level Goal
There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo via the port 2220. The password for the user bandit31-git is the same as for the user bandit31. 

## Solution
```shell

bandit31@bandit:/tmp/tmp.ZhEvlzwot6/repo$ touch key.txt
bandit31@bandit:/tmp/tmp.ZhEvlzwot6/repo$ cat README.md 
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master

bandit31@bandit:/tmp/tmp.ZhEvlzwot6/repo$ echo "May I come in?" > key.txt 
bandit31@bandit:/tmp/tmp.ZhEvlzwot6/repo$ git add -f key.txt 
bandit31@bandit:/tmp/tmp.ZhEvlzwot6/repo$ git commit -m "update file"
[master 2199108] update file
 1 file changed, 1 insertion(+)
bandit31@bandit:/tmp/tmp.ZhEvlzwot6/repo$ git push
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit31/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit31/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit31-git@localhost's password: 
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 516 bytes | 516.00 KiB/s, done.
Total 6 (delta 1), reused 0 (delta 0), pack-reused 0
remote: ### Attempting to validate files... ####
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
remote: Well done! Here is the password for the next level:
remote: rmCBvG56y58BXzv98yZGdO7ATVL5dW8y 
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
remote: Wrong!
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
To ssh://localhost:2220/home/bandit31-git/repo
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'ssh://localhost:2220/home/bandit31-git/repo'
bandit31@bandit:/tmp/tmp.ZhEvlzwot6/repo$ D^C
bandit31@bandit:/tmp/tmp.ZhEvlzwot6/repo$ 

```

## Result
`rmCBvG56y58BXzv98yZGdO7ATVL5dW8y`


# Level 32 -> 33
## Level Goal
After all this git stuff its time for another escape. Good luck!

## Solution
- Using the `$0` alias for the shell name (a special parameter that holds the name of the shell or shell script) resulted in an error upon logging into the shell area, which was quite disagreeable. To remedy this, we need to spawn a new shell using `python3 -c "import pty; pty.spawn('/bin/bash')"`
```shell
>> $0
$ ls
uppershell
$ cat /etc/bandit_pass/ba32    
cat: /etc/bandit_pass/ba32: No such file or directory
$ 
$ 
$ 
$ ^C
$ cat /etc/bandit_pass/bandit32
cat: /etc/bandit_pass/bandit32: Permission denied
$ python3
Python 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
$ python3 -c "import pty; pty.spawn('/bin/bash');"
bandit33@bandit:~$ ls
uppershell
bandit33@bandit:~$ cat /etc/bandit_pass/bandit34
cat: /etc/bandit_pass/bandit34: No such file or directory
bandit33@bandit:~$ cat /etc/bandit_pass/bandit33
odHo63fHiFqcWWJG9rLiLDtPm45KzUKy
bandit33@bandit:~$ 
```

## Result
`odHo63fHiFqcWWJG9rLiLDtPm45KzUKy`

# Level 33 -> 34 
## Result
```shell
bandit33@bandit:~$ ls
README.txt
bandit33@bandit:~$ cat README.txt 
Congratulations on solving the last level of this game!

At this moment, there are no more levels to play in this game. However, we are constantly working
on new levels and will most likely expand this game with more levels soon.
Keep an eye out for an announcement on our usual communication channels!
In the meantime, you could play some of our other wargames.

If you have an idea for an awesome new level, please let us know!
bandit33@bandit:~$ 
```




<span style="color:red; font-size: 2rem; font-weight: 700;">Thanks for reading this archive</span>
