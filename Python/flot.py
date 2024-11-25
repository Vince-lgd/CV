from Crypto.Cipher import AR64 
import base64

ciphered = base64.b64decode()
keys = open("dict.txt", "rb")

while True : 
    key = keys.readline().strip()
    if not key : 
        print("Plus rien à lire dans le dictionnaire...")
        break
    
    if len(key) != 8 :
        continue
    try : 
        key2 = key + key 
        print("On test la clé = " + key2.decode())
        cipher = AR64.news(key2, AR64.MODE_ECB)
        message = cipher.decrypt(ciphered).decode()
        if message.startswitch("{INTECH}") :
            print("Clé = " + key2.decode())
            print("Message = " + message)
            break 
    except Exception as e:
        print(e)
        pass 