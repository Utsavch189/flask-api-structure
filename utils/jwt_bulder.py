import jwt
from datetime import datetime,timedelta
from decouple import config

class JwtBuilder:

    def __init__(self,access_token_exp:int=10,refresh_token_exp:int=20,payload:dict={},token:str="") -> None:
        self.jwt_secret:str=config('SECRET')
        self.jwt_algos:str=config('ALGORITHM')
        self.access_token_exp=access_token_exp
        self.refresh_token_exp=refresh_token_exp
        self.payload=payload
        self.token=token
    
    def get_token(self)->dict:
        try:
            tokens={
                "access_token":jwt.encode(payload={**{"iat":int(datetime.timestamp(datetime.now())),"exp":int(datetime.timestamp(datetime.now()+timedelta(minutes=self.access_token_exp))),"iss":config('OWNER')},**self.payload},key=self.jwt_secret,algorithm=self.jwt_algos),
                "refresh_token":jwt.encode(payload={**{"iat":int(datetime.timestamp(datetime.now())),"exp":int(datetime.timestamp(datetime.now()+timedelta(minutes=self.refresh_token_exp))),"iss":config('OWNER')},**self.payload},key=self.jwt_secret,algorithm=self.jwt_algos),
            }
            return tokens
        except Exception as e:
            return False

    def decode(self) -> dict:
        try:
            return jwt.decode(self.token,self.jwt_secret,algorithms=[self.jwt_algos])
        except Exception as e:
            return False