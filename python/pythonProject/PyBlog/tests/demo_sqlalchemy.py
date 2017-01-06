# -*-coding:utf-8 -*-
from sqlalchemy import *


# 连接数据库
db = create_engine('sqlite:///test_sql.db')

# 数据库管理对象
metadata = MetaData(db)

# 创建表结构
# users = Table('users', metadata,
#               Column('id', Integer, primary_key=True, autoincrement=True),
#               Column('name', String(40), nullable=False, index=True),
#               Column('password', String(16)), autoload=True)
#
# users.create()


# 表对象
users = Table('users', metadata, autoload=True)


# 插入数据
# i = users.insert()
# i.execute(name='Mary', password='secret')
# i.execute({'name': 'John', 'password': 42},
#           {'name': 'Susan', 'password': 57},
#           {'name': 'Carl', 'password': 33})

# 查询数据
s = users.select()
rs = s.execute()
for row in rs:
    print(row.id, row.name, row.password)

