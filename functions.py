import hashlib
import binascii
import passlib.hash;

_example_string = 'hello!'
_example_salt   = 'salt'
_example_iv     = '12345678'

from Crypto.Cipher import DES, AES


def pVault_encode_DES(secret, password, iv):
    des1 = DES.new(secret, DES.MODE_CFB, iv)
    return des1.encrypt(password)

def pVault_decode_DES(secret, password_criptata, iv):
    des2 = DES.new(secret, DES.MODE_CFB, iv)
    return des2.decrypt(password_criptata)

def pVault_encode_AES(secret, password, iv):
    aes1 = AES.new(secret, AES.MODE_CFB, iv)
    return binascii.hexlify(aes1.encrypt(password))

def pVault_decode_AES(secret, password_criptata, iv):
    aes2 = AES.new(secret, AES.MODE_CFB, iv)
    return aes2.decrypt(binascii.unhexlify(password_criptata))

def pVault_MD5(text):
    m = hashlib.md5()
    m.update(text)
    return binascii.hexlify(m.digest())

def pVault_NT(text):
    m = passlib.hash.nthash.encrypt(text)
    return m



