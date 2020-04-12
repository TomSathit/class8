#AES-128 CBC decryption in Python
from Crypto.Cipher import AES
import Crypto.Cipher.AES
from binascii import hexlify, unhexlify

print(len('2b7e151628aed2a6abf7158809cf4f3c'))
key = unhexlify('2b7e151628aed2a6abf7158809cf4f3c')    #32 byte
IV = unhexlify('000102030405060708090a0b0c0d0e0f')     #32 byte

s = '0000000000sathit'.encode('utf-8')
print(type(s), s)
s = s.hex()
plaintext1 = unhexlify(s)

print(plaintext1)

cipher = AES.new(key,AES.MODE_CBC,IV)
ciphertext = cipher.encrypt(plaintext1)
print(hexlify(ciphertext))

decipher = AES.new(key,AES.MODE_CBC,IV)
plaintext = decipher.decrypt(ciphertext)
print(plaintext == plaintext1)                        # test if decryption was successful
print(plaintext.decode('utf-8'))
