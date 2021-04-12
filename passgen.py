import string
import random
pass_len = int(input("enter pass len: "))
if (pass_len >= 0 and pass_len <=32):
    letters = string.ascii_letters
    num = string.digits
    symbols = string.punctuation
    chars = letters + num + symbols
    password = "".join(random.sample(chars, pass_len))
    print(password)
    
else:
    print("enter valid length")