# import sqlalchemy as db
# from sqlalchemy import Column, Integer,String
# from sqlalchemy.orm import declarative_base
# from sqlalchemy.orm import sessionmaker

# engine = db.create_engine("sqlite:///employees.sqlite")
# conn = engine.connect()

# metadata = db.MetaData()
# employee = db.Table('Employee', metadata,
#             db.Column('id', db.Integer(), primary_key=True),
#             db.Column('name', db.String(255), nullable=False),
#             db.Column('address', db.String(1024), default="Nammane"),
#             db.Column('pic_id', db.String(1024), default="default")
#             )
# metadata.create_all(engine)

# Base = declarative_base()
# session = sessionmaker(bind=engine)()

# class Employeers_Company(Base):
#       __tablename__ = "employee"
#       name = Column(String)
#       id = Column(Integer, primary_key=True)
#       address = Column(String)
#       pic_id = Column(String)

#       def __init__(self, name, id, address, pic_id='default'):
#             super().__init__()
#             self.name = name
#             self.id = id
#             self.address = address
#             self.pic_id = 'default'

#       def save(self):
#             session.add(self)
#             session.commit()

# # employee4 = Employeers_Company("Srihari", 2, "JP Nagara", "default_pic")
# # session.add(employee4)
# # session.commit()

# # Get an entry by id from DB.
# employee_obj = session.query(Employeers_Company).filter_by(id=12).first()
# print(employee_obj)

import sqlalchemy as db
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

engine = db.create_engine("sqlite:///employees.sqlite")
conn = engine.connect()

metadata = db.MetaData()
employee = db.Table('Employee', metadata,
                db.Column('id', db.Integer(), primary_key=True),
                db.Column('name', db.String(255), nullable=False),
                db.Column('address', db.String(1024), default="Nammane"),
                db.Column('pic_id', db.String(1024), default="default")
                )
metadata.create_all(engine)

# Initialize a db session
Base = declarative_base()
session = sessionmaker(bind=engine)()
# Save an entry to DB.
class Employers_Company(Base):
    __tablename__ = "employee"
    name = Column(String)
    id = Column(Integer, primary_key=True)
    address = Column(String)
    pic_id = Column(String)
    def __init__(self, name, id, address, pic_id='default'):
        super().__init__()
        self.name = name
        self.id = id
        self.address = address
        self.pic_id = 'default'

    def save(self):
        session.add(self)
        session.commit()

    def __str__(self):
        return str({
            "id": self.id,
            "name": self.name,
            "address": self.address
    })

    def get_by_id(self):
        emp = session.query(Employers_Company).filter_by(id=self.id).first()
        return emp


emp = Employers_Company("Sreedhar", 41, "KS Layout")
emp


emp2 = Employers_Company("Akshay", 22, "Padmanabhanagara")
emp2

emp3 = Employers_Company("Sreedhar", 23, "KS Layout")
emp3

emp4 = Employers_Company("Nikhil", 24, "Magdi Road")
emp4

emp_g = Employers_Company("", 24, "")
print(str(emp_g.get_by_id()))

#
#employee4 = Employee_company("Srihari", 2, "JP Nagara", "default_pic")
#session.add(employee4)
#session.commit()