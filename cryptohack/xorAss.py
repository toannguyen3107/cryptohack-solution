string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
string_ord = [o for o in bytes.fromhex(string)]
for i in range(256):
	m = [o ^ i for o in string_ord]
	l = ''.join([chr(o) for o in m])
	if l[:3] == 'cry':
		print(l)
		break

