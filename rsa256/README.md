# PACTF_2017: RSA256

**Category:**
**Points:** 80
**Description:**

>According to Wikipedia, RSA 256 can be factored on modest hardware in 35 minutes. Given the encoded public key MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAIl47p5SrV3uMTsUAbwE0E+j+QynAY/CVq/Gf8IAOQy7AgMBAAE=, what is the similarly-encoded private key? The first 32 characters is the flag.

**Hint:**

>And apparently YAFU can do it in 103 seconds!

## Write-up
PyCrypto to the rescue!

[script](solve.py)

Therefore, the flag is `MIGpAgEAAiEAiXjunlKtXe4xOxQBvATQ`.
