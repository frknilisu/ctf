# PACTF_2017: RSA256

**Category:**
**Points:** 80
**Description:**

>According to Wikipedia, RSA 256 can be factored on modest hardware in 35 minutes. Given the encoded public key MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAIl47p5SrV3uMTsUAbwE0E+j+QynAY/CVq/Gf8IAOQy7AgMBAAE=, what is the similarly-encoded private key? The first 32 characters is the flag.

**Hint:**

>And apparently YAFU can do it in 103 seconds!

## Write-up
PyCrypto to the rescue!

1. Start by installing PyCrypto. This includes a lot of useful tools.
2. You need to convert the raw base64 string into a readable RSA key file. This is easily done:  
-----BEGIN PUBLIC KEY-----  
MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAIl47p5SrV3uMTsUAbwE0E+j+QynAY/CVq/Gf8IAOQy7AgMBAAE=  
-----END PUBLIC KEY-----

Save this to a file called, for example, rsa256.pub.  
[rsa256.pub](rsa256.pub)

3. Import this key into Python and extract the values of n and e:  

from Crypto.PublicKey import RSA  
key = RSA.importKey(open('rsa256.pub').read())  
print key.n, key.e  

[cry.py](cry.py)

4. Now factorize n:  
mkdir yafu  
mkdir bin  
cd yafu  
wget "https://downloads.sourceforge.net/project/yafu/1.34/yafu-1.34.zip" -O yafu.zip  
unzip yafu.zip  
chmod 755 yafu  
mv yafu ../bin  
run yafu  

factor(n)

Call the larger one p and the smaller one q.

5. generate a private key:  
Call pqe2rsa() with the values of p and q from step 4 and the value of e from step 3, and you should get a private key.

[solve.py](solve.py)

Therefore, the flag is `MIGpAgEAAiEAiXjunlKtXe4xOxQBvATQ`.
