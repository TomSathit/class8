#AES-128 CBC decryption in Python
from Crypto.Cipher import AES
import Crypto.Cipher.AES
from binascii import hexlify, unhexlify

key = unhexlify('2b7e151628aed2a6abf7158809cf4f3c')    #16 byte
IV = unhexlify('000102030405060708090a0b0c0d0e0f')     #16 byte

plaintextbegin = '0000000000sathit'.encode('utf-8') 
print(" plaintextbegin encode utf-8 --> ",type(plaintextbegin), plaintextbegin)

cipher = AES.new(key,AES.MODE_CBC,IV)
ciphertext = cipher.encrypt(plaintextbegin)
print("hexlify ciphertext--> ", hexlify(ciphertext))

decipher = AES.new(key,AES.MODE_CBC,IV)
plaintext = decipher.decrypt(ciphertext)
print(plaintext)
textstr = plaintext.decode('utf-8')
print(type(textstr), textstr)