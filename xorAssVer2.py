pass_secret = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
tmp_key = b'crypto{1'
key = b'myXORkey'
pass_secret_byte = bytes.fromhex(pass_secret)
xor_arr = []
for i in range(len(pass_secret_byte)):
    xor_arr.append(pass_secret_byte[i] ^ key[i % len(key)])
xor_key = "".join(chr(o) for o in xor_arr)
print(xor_key)
