# solution
 - analysis the trafic when you send login request you see the request have form http://<target_host>/.../<base64 encode>
 - You decode the crypt, you see
 ```shell
 ┌──(toan㉿kali)-[~]
└─$ echo "bF90aGVfd2F5XzI1YmJhZTlhfQ==" | base64 -d  
l_the_way_25bbae9a}                                                                             
┌──(toan㉿kali)-[~]
└─$ echo "cGljb0NURntwcm94aWVzX2Fs" | base64 -d    
picoCTF{proxies_al                                                                             
┌──(toan㉿kali)-[~]
└─$ mkdir -p  note_hackthebox_cryptohack_ctf/picoCTF/findme
 ```