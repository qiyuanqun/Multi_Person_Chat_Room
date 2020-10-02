from pymysql import connect
from database_modular import *


class DB(object):
    '''数据库操作管理类'''

    def __init__(self):
        # 连接数据库
        self.conn = connect(host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
                )

        # 获取游标
        self.cursor = self.conn.cursor()

    def close(self):
        '''释放数据库资源'''
        self.cursor.close()
        self.conn.close()

    def get_one(self, sql):
        self.cursor.execute(sql)
        query_result = self.cursor.fetchone()
        if not query_result:
            return None
        fileds = [filed[0] for filed in self.cursor.description]
        return_data = dict()
        for filed, value in zip(fileds, query_result):
            return_data[filed] = value
        return return_data

if __name__ == '__main__':
    db = DB()
    data = db.get_one('select * from user where id=1')
    print(data)
    db.close()