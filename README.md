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
### Another use of generator

```
>>  def gen():
	    for i in range(3):
		yield i        
>>  g=gen()
>>  g.__next__()
0
>>  g.__next__()
1
>>  g.__next__()
2
>>  g.__next__()
```
### Iterator 

```
>>  string='hello'
>>  s=iter(string)
>>  s.__next__()
'h'
>>  s.__next__()
'e'
>>  s.__next__()
'l'
>>  s.__next__()
'l'
>>  s.__next__()
'o'
```

### Python debuger

```
import pdb
x=[1,2,3]
y=2
z=3
result_one=y+z
pdb.set_trace()
result_two=y+x
```
### Regular expression regex or re

```
>>  string="hello world 123 456"
>>  pattern="123"
>>  import re
>>  re.search(pattern,string)
<re.Match object; span=(12, 15), match='123'>
>>  match=re.search(pattern,string)
>>  match.span()
(12, 15)
>>  match.start()
12
>>  match.end()
15
>>  string="hello world 123 456 123"
>>  re.findall(pattern,string)
['123', '123']
>>  match=re.search(pattern,string)
>>  for match in re.finditer(pattern,string):
    	print(match)
<re.Match object; span=(12, 15), match='123'>
<re.Match object; span=(20, 23), match='123'>
```
<img src="https://github.com/Psingh12354/Python-Classes/blob/main/img1.jpeg" width="650" height="300">
<img src="https://github.com/Psingh12354/Python-Classes/blob/main/img2.jpeg" width="650" height="300">

### Some more about re

```
>>  import re
>>  text="My phone number is 405-555-7777"
>>  phone=re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
>>  phone
<re.Match object; span=(19, 31), match='405-555-7777'>
>>  phone.group()
'405-555-7777'
>>  # using quantifiers
>>  phone=re.search(r'\d{3}-\d{3}-\d{4}',text)
>>  phone
<re.Match object; span=(19, 31), match='405-555-7777'>
>>  phone_pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4}))

### Compile run the multiple search at once

>>  phone_pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
>>  result=re.search(phone_pattern,text)                       
>>  result.group()                       
'405-555-7777'
>>  result.group(1)                       
'405'

### Operator Or(|), wildcard(.), 

>>  string="Hello dog it's me"
>>  re.search(r'cat|dog',string) #| this is or symbol
<re.Match object; span=(6, 9), match='dog'>
>>  re.search(r'.e',string) #.e is a wildcard similar to like (_) operator can use multiple for multiple single char
<re.Match object; span=(0, 2), match='He'>
>>  string="Hello 1 dog it's me"
>>  re.findall(r'^\d',string) #^\d it's mean the string start with number
[]
>>  string="1 Hello dog it's me"
>>  re.findall(r'^\d',string) #^\d it's mean the string start with number
['1']
>>  string="Number ends with 2"
>>  re.findall(r'\d$',string) #^\$ it means number at last
['2']
>>  string= "there are 3 number 35 inside this sentence"
>>  pattern=r'[^\d]' # to exclude numbers
>>  re.findall(pattern,string)
['t', 'h', 'e', 'r', 'e', ' ', 'a', 'r', 'e', ' ', ' ', 'n', 'u', 'm', 'b', 'e', 'r', ' ', ' ', 'i', 'n', 's', 'i', 'd', 'e', ' ', 't', 'h', 'i', 's', ' ', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e']
>>  ''.join(re.findall(pattern,string))
'there are  number  inside this sentence'
>>  pattern=r'[^\d]+' #
>>  re.findall(pattern,string)
['there are ', ' number ', ' inside this sentence']
>>  string="This is, punctuation. marks?"
>>  re.findall(r'[^!,.?]+',string)  #it remove all punctuation marks
['This is', ' punctuation', ' marks']
>>  string="only find hyphen-word in this-sentence"
>>  re.findall(r'[\w]+-[\w]+',string)
['hyphen-word', 'this-sentence']
```
