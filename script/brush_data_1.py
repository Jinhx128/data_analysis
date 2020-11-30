# -*- coding: utf-8 -*-
import datetime
import pymysql
from apscheduler.schedulers.blocking import BlockingScheduler
import hashlib

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


def my_md5(s, salt=''):      #加盐，盐的默认值是空
    s = s+salt
    news = str(s).encode()    #先变成bytes类型才能加密
    m = hashlib.md5(news)     #创建md5对象
    return m.hexdigest()    #获取加密后的字符串


Base = declarative_base()

#以User表为例
class User(Base):
    # 数据库表名
    __tablename__ = 'users'

    # 这个MySQL使用的主键
    # id = Column(Integer, primary_key=True, autoincrement=True)
    # 这个是Oracle使用的主键定义方法，MySQL也通过，推荐使用这个，数据库更换时，可以不用修改代码
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)

    name = Column(String(30))
    fullname = Column(String(30))
    nickname = Column(String(30))

    def __repr__(self):
        """命令行运行时，打印对象显示的值调用"""
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)


# echo=True表示日志打印出来
engine = create_engine("mysql://django:django@192.168.2.138:3306/testDatabase", encoding='utf-8', echo=False)

Session = sessionmaker(bind=engine)  # 产生会话
Session.configure(bind=engine)  # 往Session配置可用的会话引擎
session = Session()


def brush_mysql():
    # 连接database
    conn = pymysql.connect(host='xxx', user='xxx', password='xxx', database='xxx', charset='utf8')
    # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    f = 'mb_dep_doctor_info'
    t = 'remind_schedule'
    print('开始刷数据！')
    # 修改数据的SQL语句
    unit_id + dep_id + doctor_id + to_date + time_type
    sql1 = 'select unit_id, dep_id, doctor_id, to_date, time_type, from mb_dep_doctor_info order by dep_doctor_id desc limit 2000'
    sql2 = 'insert into remind_schedule (id, unit_id, dep_id, doctor_id, sch_date, time_type, sch_state, audit_state, change_log, modified_date) ' \
          'values ()'
    try:
        # 执行SQL语句
        execute = cursor.execute(sql1)
        results = cursor.fetchall()  # 获取查询的所有记录
        # 遍历结果
        for row in results:
            id = row[0]
            name = row[1]
            password = row[2]
            print(id, name, password)
    except Exception as e:
        # 有异常，回滚事务
        conn.rollback()
    print('-' * 100)
    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    conn.close()


scheduler = BlockingScheduler()
scheduler.add_job(brush_mysql, 'cron', second='0', minute='0', hour='1')
print('python刷数据脚本启动！')
scheduler.start()