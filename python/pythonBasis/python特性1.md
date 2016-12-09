### python特性1--一切都是对象

#### 函数特性
1. 函数可以赋值给变量
```python
	def func(name):
		print(name)
	a = func
	a('phb')
```
2. 函数可以作为另一个函数的参数
```python
	def func(name):
		print(name)
	
	def wrap(func, name):
		return func(name)

	wrap(func, 'phb')
```
3. 函数可以作为另一个函数的返回值
```python
	def func(name):
		print(name)
	
	def wrap():
		return func
	
	a = wrap()
	a('phb')
```
4. 函数可以定义在一个函数内部
```python
	def func(name):
		return name

	def decor_func(func_name):
		def wrapper(name):
			print('<p>{}<p>'.format(func_name(name)))
		return wrapper

	f = decor_func(func)
	f('phb')	
```
5. function can return multi values
```python
    def returnabc(a, b, c):
        return a, b, c

    i, j, k = returnabc(1, 2, 3)
    print(i, j, k)
```

#### python装饰器
	装饰器可以在不改变目标函数的代码上增强目标函数的功能， 本质是将目标函数作为参数传入到一个装饰函数中，并由装饰函数返回一个新的函数供使用者调用。 python的@功能
```python
	def en_func(func_name):
		def wrapper(name):
			print('<strong>{}<strong>'.format(func_name(name)))
		return wrapper

	@en_func
	def func(name):
		return name

	def func2(name):
		return name


	func('phb')
	'''equals'''
	en = en_func(func2)
	en('phb')
```

#### 上下文管理器
	上下文管理器(ContextManager) 主要用于为一个对象请求和释放资源。<br/>
	为一个对象创建一个上下文管理器 主要是重写对象的 __enter__方法 和 __exit__方法。  
	通过  with <object> as <returned by __enter__>:  语法使用一个对象的上下文管理器。 对象的__enter__方法在语句块开始前调用， __exit__方法在语句块结束时调用
```python
	class Log(object):
		def __init__(self, msg):
			self._msg = msg

		def __enter__(self):
			print('Log Enter')
			return self             

		def __exit__(self, exc_type, exc_val, exc_tb):
			print('Log Exit')

		def i(self, msg):
			print(msg)


	def get_log(msg):
		return Log(msg)


	with get_log('hello') as log:
		log.i('hello, phb')
```

#### 生成器和迭代器
```python
	# 列表生成器
	a = [i**2 for i in range(10) if i > 0]
	print(a)  # a是一个列表
	a = (i**2 for i in range(10) if i > 0)
	print(a)  # a是一个生成器

	# generator
	# 生成器也是一个迭代器
	a = (i**2 for i in range(10) if i > 0)
	for i in a:
		print(i)
	# 生成器保存的数据生成的算法，而不是数据本身，每调用一次next(), 生成一个数据, 节省内存

	# 生成器只能遍历一次
	for i in a:
		print(i)  # 没有任何数据

	# yield 实现 生成器  如果一个函数定义中包含 yield 关键字， 那么这个函数就不再是一个普通函数， 而是一个generator, 函数在每次调用next()的时候执行， 遇到yield语句返回， 再次执行时从上次返回的yield语句处继续执行, 遇到函数末尾则结束
	def func():
		a = 1
		while a<10:
			yield a
			a = a + 1

	for i in func():
		print(i)

	# 一个斐波那契数列的例子 f(n) = f(n - 1) + f(n - 2)  , n1 = 1, n2 = 1
	def fib(max):
		n, a, b =  0, 0, 1
		while n < max:
			yield b
			a, b = b, a + b
			n = n + 1

	for i in fib(10):
		print(i)
```

#### 交换两个数字
```python
	a = 1
	b = 2
	a, b = b, a
	print(a,b)
```