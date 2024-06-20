from database.connection import getDb
from utils import JwtBuilder,hash_password

class Query:

    @staticmethod
    def register(name:str,email:str,password:str)->dict:
        conn=getDb()
        cur=conn.cursor()
        try:
            print(Query.getUser(email))
            if Query.getUser(email):
                raise Exception("user already exists!")
            
            else:
                q="INSERT INTO User(name,email,password) VALUES('%s','%s','%s')"%(name,email,hash_password(password))
                cur.execute(q)
                conn.commit()
                payload={"name":name,"sub":email}
                tokens=JwtBuilder(payload=payload).get_token()
                return tokens
        except Exception as e:
            print(e)
            conn.rollback()
            raise Exception(str(e))
    
    @staticmethod
    def getUser(email:str):
        conn=getDb()
        cur=conn.cursor()
        try:
            q="SELECT * FROM User WHERE email='%s'"%(email,)
            res=cur.execute(q)
            return res.fetchall()
            
        except Exception as e:
            print(e)
            raise Exception(str(e))
    
    @staticmethod
    def get_foods(dish_name:str):
        conn=getDb()
        cur=conn.cursor()
        try:
            dish='%'+dish_name+'%'
            q="SELECT * FROM Foods WHERE LOWER(recipe) LIKE '%s'"%(dish,)
            res=cur.execute(q)
            return res.fetchall()
            
        except Exception as e:
            print(e)
            raise Exception(str(e))