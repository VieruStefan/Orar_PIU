from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
metadata_obj = MetaData()
engine = create_engine('mysql+pymysql://user:passwduser@localhost/PIU')
Session = sessionmaker(bind=engine)