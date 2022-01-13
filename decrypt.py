import json
import base64
import des
import sys

def decode(hash):
	hash = base64.b64decode(hash.encode('utf-8'))
	key = des.DesKey(b"7ly6UznJ")
	return key.decrypt(hash, initial=b"XuVUm5fR", padding=True).decode('utf-8')

if len(sys.argv) < 2:
    print("usage: python3 decrypt.py <hash>")
    sys.exit(0)

print(decode(sys.argv[1]))