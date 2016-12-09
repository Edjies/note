### python特性2

#### __*args and **kwargs__
```python
	# args用于显示非键值对的参数列表
	def show(*args):
		for i in args:
			print(i)


	# kwargs用于显示键值对形式的 参数列表
	def show2(**kwargs):
		for key, value in kwargs.items():
			print('{}={}'.format(key, value))

	show(1, 2, 3, 4, 5, 6, 7, 8)
	show2(name='hello', tow='she')
```


#### __三元运算符__ 
`<true value> if <true condition> else <false value>`


#### __mutable 和 immutable__
对imutable对象的改变会创建一个新的对象

####  __slots__
一般情况下， Class 用一个Dict来保存其属性。 但这可能会浪费一定的内存。 <br/>
通过__slots__可以让Class分配固定的内存来保存其属性，而不是使用一个Dict。<br/>
```python
	class Person(object):
		__slots__ = ['name', 'age', 'address', 'phone']   # 明确指定Person类具有的属性

		def __init__(self):
			self.name = 'phb'
			self.age = '12'
			self.address = 'adfasdf'
			self.phone = '129338'
``` 

#### __lambda表达式__
lambda <arguments> : manipulate(arguments)
```python
	add = lambda x, y: x + y

	print(add(3, 5))
	# Output: 8
```

#### __global关键字__
使一个在函数内部定义的变量为全局变量（一般不常用）
