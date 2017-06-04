from Crypto.PublicKey import RSA
key = RSA.importKey(open('rsa256.pub').read())
print key.n, key.e