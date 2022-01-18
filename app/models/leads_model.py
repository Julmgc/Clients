import re
from dataclasses import dataclass
from datetime import date, datetime
from app.configs.database import db
from flask import current_app
from sqlalchemy import Column, Date, String
from sqlalchemy.sql.sqltypes import DateTime, Integer


# - trabalhar com as seguintes EXCEÇÕES da API:
# - campo não existe, campo faltando, dado de um campo em formato inválido
# - EXCEÇÕES DO SQL:

#     -usuário não existe

#     EXCEÇÕES DE REGRAS DE NEGÓCIO

#     -ex: pediram data em formato específico, ex 22-01-2021 22:12:04

#     -não permitir data do futuro
# pode pegar a mensagem do TypeError as e e return str(e)

# verificar cada um dos métodos pra ver se eles precisam mesmo existir
# se não rola de chamar direto pelo flask_SQLAlchemy e ORM que nem o Lucas fez na demo

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
    creation_date = Column(DateTime, nullable=False)
    last_visit = Column(DateTime, nullable=True)
    visits = Column(Integer, nullable=True, default=1)
    
    
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email   
        self.phone = phone
        self.creation_date = datetime.utcnow()
        self.last_visit = datetime.utcnow()
        self.visits = 1
        
        
    def query_to_json(self):
        return {"name": self.name, "email":self.email, "phone": self.phone, "creation_date": self.creation_date, "last_visit": self.last_visit, "visits": self.visits} 

    @staticmethod
    def check_keys(**kwargs):
      keys = ["name", "email", "phone"]
      data_keys = [i for i in kwargs.keys()]
      check_if_values_are_strings = [i for i in kwargs.values() if type(i) == str]
      if sorted(keys) == sorted(data_keys) or len(check_if_values_are_strings) != 3:
        return True

    @staticmethod
    def check_phone_format(**kwargs):
      phone = kwargs["phone"] 
      check_match = re.fullmatch(r"([0-9]{2,3})?(\([0-9]{2}\))([0-9]{5})-([0-9]{4})", phone)
      if check_match == None:
        return True

    @staticmethod
    def insert_user(**kwargs):
      lead = Leads(**kwargs)
      session = current_app.db.session
      session.add(lead)
      session.commit()
      data = lead.query_to_json()
      return data

    @staticmethod    
    def get_all_users():

      data = Leads.query.all()
      data_to_json = [ vaccine.query_to_json() for vaccine in data]
      sorted_data =  sorted(data_to_json, key=lambda k: k['visits'], reverse=True) 
      return sorted_data
            
    @staticmethod
    def check_data_key(**kwargs):
        data_keys = [i for i in kwargs.keys()]
        if len(data_keys) == 1 and (data_keys[0] == "email") and (type(data_keys[0]) == str):
            return True

    @staticmethod
    def patch_user_data(**kwargs):
        user = Leads.query.filter_by(email=kwargs["email"]).first()
        user.last_visit = datetime.utcnow()
        user.visits += 1
        db.session.commit()
        data = user.query_to_json()
        return data

    @staticmethod    
    def delete_user_data(**kwargs):
        user = Leads.query.filter_by(email=kwargs["email"]).first()  
        if user == None:
          return False      
        db.session.delete(user)
        db.session.commit()
        data = user.query_to_json()
        return data










