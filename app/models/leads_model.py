from dataclasses import dataclass
from datetime import date, datetime, timedelta
from app.configs.database import db
from sqlalchemy import Column, Date, String
from sqlalchemy.sql.sqltypes import Integer
import re
# id: Inteiro e chave primária;

@dataclass
class Leads(db.Model):
    name = str
    email = str
    phone = str
    creation_date = date
    last_visit = date
    visits = int

    __tablename__ = 'leads_table'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True )
    phone = Column(String, unique=True, nullable=False)
    creation_date = Column(Date(), nullable=False)
    last_visit = Column(Date(), nullable=True)
    visits = Column(Integer, nullable=True, default=1)
    
    
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email   
        self.phone = phone
        self.creation_date = datetime.utcnow()
        self.last_visit = datetime.utcnow() + timedelta(days=90)
        self.visits = 1
        
    def query_to_json(self):
        return {"name": self.name, "email":self.email, "phone": self.phone, "creation_date": self.creation_date, "last_visit": self.last_visit, "visits": self.visits} 

    def is_phone_Valid(s):
        Pattern = re.compile("^\(?[1-9]{2}\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$")
        # return Pattern.match(s)
        return re.fullmatch(Pattern, s)
    # Driver Code
    # s = "347873923408"
    # if (isValid(s)):
    #     print ("Valid Number")    
    # else :
    #     print ("Invalid Number")