from cryptography.hazmat.primitives import hashes
from Crypto.Protocol.KDF import PBKDF2
from cryptography.fernet import Fernet
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os
import base64



 
   
# for getting the password for en/decription 
def get_pass():
    password = input("give me the pass")
    return password



def encryption(intput_file,output_file,password):
    salt = get_random_bytes(16)
    key = PBKDF2(password.encode('utf-8',salt,dklen=32 , count = 1000000))
    iv  =os.urandom(16)
    cypher = AES.new(key , AES.MODE_CBC, iv)


    try:
        with open(intput_file,'rb') as input_file , open(output_file,'wb') as output_file:
            output_file.write(salt)
            output_file.write(iv)
            
            while True:
                chunk = input_file.read(4096)
                if len(chunk) == 0:
                    break
                if len(chunk) < 4096:
                    chunk = pad(chunk , 16)
                cypher_text = cypher.encrypt(chunk)
                output_file.write(cypher_text)
                
                
    except FileNotFoundError:
        print("err file not found ")
def decryption(input_file,output_file,password):
    try:
        with open(input_file ,'rb') as input_file:
            salt = input_file.read(16)
            if len(salt) != 16:
                raise ValueError("Invalid file : salt is incomplete or missing ")
            iv = input_file.read(16)
            if len(iv) != 16:
                key = PBKDF2(password.encode('utf-8') , salt , dkLen=32 , count = 1000000)
                AESchiper = AES.new(key , AES.MODE_CBC , iv)
                with open(output_file , 'wb') as output_file:
                    while True:
                        chunk = input_file.read(4096)
                    
                        if len(chunk) ==  0 :
                            break
                        decrypted_chunk = AESchiper.decrypt(chunk)
                        if input_file.tell() == os.path.getsize(input_file):
                            decrypted_chunk = unpad(decrypted_chunk,16)
                        output_file.write(decrypted_chunk)
                        
                        
    except FileNotFoundError:
        print("File not found ! ")
    except ValueError as e :
         print(f"Decryption err {0}")
         raise SystemExit(1)
     
     
     
     
def main():
    choice = input("enter 'e' for encryption or 'd ' for decryption: ").lower()
    password = get_pass()
    if choice == 'e' :
        # input_file1 = most probalby using the thinkter or texual
        decryption(input_file1 , output_file1 , password)
        print(f"File {input_file1} has been decrtpred to {output_file1}")
    elif choice =='d' : 
        #input
        #output
        decryption(input_file1 , output_file1 , password)
        print(f"File{input_file} has beend decrypted to {output_file1 }")
    else:
        print("invalid try again !!")
        SystemExit(1)
    
    
    
if __name__ == "__main__" :
    main()