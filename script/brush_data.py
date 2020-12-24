# -*- coding: utf-8 -*-
import datetime
import pymysql
from apscheduler.schedulers.blocking import BlockingScheduler


def brush_mysql():
    # 连接database
    conn = pymysql.connect(host='xxx', user='xxx', password='xxx', database='xxx', charset='utf8')
    # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    tables = ['article', 'book', 'book_note']
    count = 10
    print('到点了，开始刷数据！')
    for item in tables:
        # 修改数据的SQL语句
        sql = 'update {} set read_num = read_num + {} where publish = 1'.format(item, count, count)
        try:
            # 执行SQL语句
            execute = cursor.execute(sql)
            # 提交事务
            conn.commit()
            print('{}-{}表更新了{}条数据，每条数据阅读量加{}！'.format(
                datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), item, execute, count))

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