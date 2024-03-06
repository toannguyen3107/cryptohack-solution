#message = "6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222e93c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7"
message = "6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"
bmsg = bytes.fromhex(message)
#print(bmsg)

def decrypt(enc):
	pt = ''
	for c in enc:
		for i in range(1,179):
			if (123*i + 18)%256 == c:
				pt += chr(i)
	return pt
if __name__ == '__main__':
	plaintext = decrypt(bmsg)
	print(plaintext)
