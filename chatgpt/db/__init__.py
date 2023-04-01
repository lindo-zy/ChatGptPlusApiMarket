#!/usr/bin/python3
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chatgpt.conf.mysettings import settings
from chatgpt.models.users import Base

# engine = create_engine('mysql+pymysql://root:123456@127.0.0.1/chatgpt')
engine = create_engine(
    f'mysql+pymysql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}/{settings.DATABASE}')
Session = sessionmaker(bind=engine)
db_session = Session()


def create_all():
    Base.metadata.create_all(engine)
