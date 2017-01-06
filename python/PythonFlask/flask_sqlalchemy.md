### Flask--Sqlalchemy依赖包

1. [定义模型](#p1)
2. [执行数据库操作](#p2)

<span id='p1'>定义模型</span>
```python
User(db.model):
	__tablename__= 'users'  # 定义表名
	id = Column(db.Integer, primary_key=True)
	dc
```

<span id='p2'>数据操作</span>
