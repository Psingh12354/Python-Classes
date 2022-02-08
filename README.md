# Python-Classes

### Normal function

```
def myfunc(a,b,c=0):
    return sum((a,b,c))*0.05
>>myfunc(10,20)
>>1.5
>>myfunc(10,20,30,40) #will give you an error 3 param but take 4 parama
```

### *args args

```
>> def myfunc(*args): #*args return tuple of parameter
    return sum(args)*0.05
>> myfunc(10,20,30,40) #here you can pass n number of parameter
```

### **kwargs

```
>>  def myfunc(**kwargs):
        print(kwargs)
        if 'fruit' in kwargs:
            print('My fruit is {}'.format(kwargs['fruit']))
        else:
            print("No fruit nor vege")

        
>>  myfunc(fruit='apple',vege='tomatto',nice='hi')
**output
{'fruit': 'apple', 'vege': 'tomatto', 'nice': 'hi'}
My fruit is apple
```

### scope in function

```
>>  def func1(x):
        print(x)
        x=10
        print(x)
        def func2():
            x=20
            print(x)
        func2()

    
>>  func1(5)
5
10
20
```

### Use of Str in classes

```
>>  class Dog():
        def __init__(self,breed):
            self.breed=breed
        def __str__(self):
            return f"{self.breed}"

    
>>  a=Dog('Desi')
>>  a
<__main__.Dog object at 0x000002CB881757E0>
>>  print(a)
Desi
```

### Some more code related to class

```
>>  class Dog():
        def __init__(self,author,num):
            self.author=author
            self.num=num
        def __str__(self):
            return f"{self.author}"
        def __len__(self):
            return self.num
        def __del__(self):
            print("Something deleted")
     
>>  b=Dog('PK',20)
>>  b
<__main__.Dog object at 0x000002CB88174310>
>>  print(b)
PK
>>  print(len(b))
20
>>  del b
b
```
### Why decorator

```
### In this code we can call hello function but can't directly call greet and welcome so we go for decorator
>>  def hello():
        print("hello")
        def greet():
            return "\t greet"
        def welcome():
            return '\t\t Welcome'
        print(greet())
        print(welcome())    
>>  hello()
hello
	 greet
		 Welcome
```

### Decorator
```
>>  def original_func():
    	print('hello')
>>  def new_decorator(orignal_func):
	    def wrap_func():
		print("Some extra code")
		original_func()
		print('Some more extra code')
	    return wrap_func()

>>  decorated_func=new_decorator(func_need_decorator)
Some extra code
hello
Some more extra code
>>  @new_decorator
    def func_need_decorator():
    print("Decorated")
Some extra code
hello
Some more extra code
```

### Without generator

```
>>  def without_gen(n):
	    result=[]
	    for i in range(n):
		result.append(i**3)
	    return result

>>  without_gen(10)
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```

### With Generator

```
>>  def generator(n):
	    for i in range(n):
		yield i**3
        
>>  for i in generator(10):
	    print(i)
0
1
8
27
64
125
216
343
512
729
```
### Fibonacci number

```
>>  def fibo(n):
	    a=1
	    b=1
	    for i in range(n):
		yield a
		a,b=b,a+b

        
>>  for i in fibo(10):
    	print(i)

    
1
1
2
3
5
8
13
21
34
55
```
### Simple generator
```
>>  def gen(n):
	    for i in range(n):
		yield i

        
>>  for i in gen(10):
    	print(i)
```
