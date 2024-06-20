import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify(password:str,hashed_password:str):
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
        return True
    else:
        return False

if __name__=="__main__":
    print(hash_password('abc'))
    print(verify('abcd','$2b$12$AsI9m8hhwBsAo67eT2uyue6x6MsKC490g69IbuuQJsP1eEKgnJ2qe'))