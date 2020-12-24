# -*- coding: utf-8 -*-
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, text
from sqlalchemy.orm import sessionmaker

import hashlib
import pymysql

pymysql.install_as_MySQLdb()

# echo=True表示日志打印出来
engine = create_engine("mysql://user:passw@xxx:3306/database?charset=utf8", encoding='utf8', echo=False)

Base = declarative_base()


class mb_dep_doctor_info(Base):
    # 数据库表名
    __tablename__ = 'mb_dep_doctor_info'

    # 字段
    dep_doctor_id = Column(Integer, Sequence('dep_doctor_id'), primary_key=True)
    doctor_id = Column(Integer())
    dep_id = Column(Integer())
    unit_id = Column(String(100))

    def __repr__(self):
        """命令行运行时，打印对象显示的值调用"""
        return "<mb_dep_doctor_info(dep_doctor_id='%s', doctor_id='%s', dep_id='%s, unit_id='%s')>" % (
        self.dep_doctor_id, self.doctor_id, self.dep_id, self.unit_id)


Session = sessionmaker(bind=engine)  # 产生会话
Session.configure(bind=engine)  # 往Session配置可用的会话引擎
session = Session()

# 2.2、返回列表
users = session.query(mb_dep_doctor_info).from_statement(text(
    'select dep_doctor_id, unit_id, dep_id, doctor_id from mb_dep_doctor_info order by dep_doctor_id desc limit 2000')).all()
for i in users:
    id = my_md5(i)
    print('数据：', i)

session.add_all(users)

session.commit()

def my_md5(s, salt=''):      #加盐，盐的默认值是空
    s = s+salt
    news = str(s).encode()    #先变成bytes类型才能加密
    m = hashlib.md5(news)     #创建md5对象
    return m.hexdigest()    #获取加密后的字符串