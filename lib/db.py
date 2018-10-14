#coding:utf-8
import pymysql
import sys
sys.path.append("..") #提升包搜索路径到项目路径
from config import confing as cf

'''数据库操作'''

#获取连接方式
def get_conn():
    conn =pymysql.connect(host=cf.db_host,
                          port=cf.db_port,
                          user=cf.db_user,
                          password=cf.db_password,
                          db=cf.db,
                          charset='utf8') # 不行写utf-8
    return conn
#查询操作

def db_query(sql):
    conn = get_conn()
    cur =conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cf.logging.debug(sql)
    cf.logging.debug(result)
    cur.close()
    conn.close()
    return  result

#修改操作

def db_change(sql):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        cf.logging.error(str(e))
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    result = db_query("select * from user where name='张三'")
    print(result)