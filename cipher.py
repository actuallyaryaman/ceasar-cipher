import random
import time

def print_with_typing_effect(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()


def encrypt(message,n):
    result=""
    
    for i in range(len(message)):
        char=message[i]
        
        if (char.isupper()):
            result+=chr(ord(char)+n-65%26+97)
        
        else:
            (char.islower())
            result+=chr(ord(char)+n-65%26+97)
    return result

def encrypt(message,n):
    result=""
    
    for i in range(len(message)):
        char=message[i]
        
        if (char.isupper()):
            result+=chr(ord(char)+n+65%26+97)
        
        else:
            (char.islower())
            result+=chr(ord(char)+n+65%26+97)
    return result
print_with_typing_effect("do you want to encrypt(1) or decrypt(2)?")
endec=input()
print_with_typing_effect("enter your message: ")
message=input()
n=random.randint(0, 1000)
if endec=="1":
    print_with_typing_effect(encrypt(message, n))
elif endec=="2":
    print_with_typing_effect(decrypt(message, n))
else:
    print_with_typing_effect("Invalid input")
