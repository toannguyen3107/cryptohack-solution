key23 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
key123flag = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"

key123 = int(key23, 16) ^ int(key1, 16) 
flag = key123 ^ int(key123flag, 16)
x = hex(flag)[2:]
print(bytes.fromhex(x))
