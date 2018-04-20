# -*- coding:utf-8 -*-
# 访问mysql和redis，验证与里面的user name 和password是否正确
import sys
import pymysql
import redis

# 访问mysql数据库
def con_mysql(sql):
    db=pymysql.connect(
    host='47.106.144.34',
    user='root',
    passwd='1221',
    port=3306,
    db='redis',
    charset='utf8'
    )
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return data

def  con_redis(name, passwd):
    r = redis.Redis(host='47.106.144.34', port=6379,
    password='jy2190883')
    r_name = r.hget('user','name')
    r_passwd = r.hget('user', 'password')
    print(r_name, r_passwd)
    r_name = r_name.decode('utf8')
    r_passwd =r_passwd.decode('utf8')
    if name == r_name and passwd == r_passwd:
        return True, '登录成功'
    else:
        return False, '登录失败'


if __name__ == '__main__':
    # 获取传入的姓名和密码参数
    name = sys.argv[1]
    passwd = sys.argv[2]
    # 传入redis中，进行校验
    result = con_redis(name, passwd)
    if not result[0]:
    # 查询mysql数据库
        sql = '''select * from test where name="%s" 
             and password="%s"''' % (name, passwd)
        data = con_mysql(sql)
        if data:
            r = redis.Redis(host='47.106.144.34', port=6379,
         password='jy2190883')
            r.hset('user','name',name)
            r.hset('user','passwd',passwd)
            print('刷新redis,登录成功')
        else:
            print('用户名和密码错误')
    else:
        print('redis中数据正确,登录成功')