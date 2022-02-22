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

### How to remove data using pop and store it in third variable
```
>>  lis=[1,2,3,4,5]
>>  r=lis.pop(lis.index(2))
>>  r
2
>>  lis
[1, 3, 4, 5]
>>  lis.append(r)
>>  lis
[1, 3, 4, 5, 2]
```
### Csv
```
#read csv

>>  import csv
>>  data=open('file.csv')
>>  csv_data=csv.reader(data)
>>  csv_data
<_csv.reader object at 0x000001A987422E60>
>>  data_lines=list(csv_data)
>>  data_lines
[['Name', ' Age'], ['Priyanshu', ' 21'], ['Singh', '21']]
>>  data=open('file.csv',encoding='utf-8')
>>  len(data_lines)
3
>>  data_lines[0]
['Name', ' Age']
>>  for line in data_lines[:5]:
        print(line)
['Name', ' Age']
['Priyanshu', ' 21']
['Singh', '21']
>>  data_lines[1][1] #row 1 and col 1
' 21'
>>  data_lines[1][0] #row 1 col 0
'Priyanshu'

# write csv

>>  file_out=open('save_file.csv',mode='w',newline='') #can use mode='a' if doesno't want to overwrite the file 
>>  csv_write=csv.writer(file_out,delimiter=",")
>>  csv_write.writerow(['Name','Age']) # to add a single row
10
>>  csv_write.writerows([['Name','Age'],['Priyanshu',21],['Singh',21]]) # to add a multiple rows
>>  file_out.close()
```
### PDF
```
>>  pip install PyPDF2 #cmd
>>  import PyPDF2
>>  f=open('file.pdf','rb')
>>  pdf_reader=PyPDF2.PdfFileReader(f)
>>  pdf_reader.numPages # count no of pages
6
>>  page_one=pdf_reader.getPage(0) #read page 1
>>  page_one
{'/Contents': IndirectObject(7, 0), '/MediaBox': [0, 0, 612, 792], '/Parent': IndirectObject(2, 0), '/Resources': {'/ExtGState': {'/GS9': IndirectObject(9, 0)}, '/Font': {'/FT10': IndirectObject(10, 0), '/FT15': IndirectObject(15, 0)}, '/XObject': {'/IM8': IndirectObject(8, 0)}}, '/Type': '/Page'}
>>  page_one_text=page_one.extractText()
>>  page_one_text #if gives a empty string check for other library rather than PyPDF2
''
>>  first_page=pdf_reader.getPage(0)
>>  type(first_page)
<class 'PyPDF2.pdf.PageObject'>
>>  pdf_writer=PyPDF2.PdfFileWriter()
>>  pdf_writer.addPage(first_page)
>>  pdf_output=open('NewPdfFile.pdf','wb')
>>  pdf_writer.write(pdf_output)
>>  f.close()
>>  pdf_output.close()
```

### String
```
>>  s='hello world'
>>  s.capitalize()
'Hello world'
>>  s.upper()
'HELLO WORLD'
>>  s.lower()
'hello world'
>>  s.count('i')
0
>>  s.find('o')
4
>>  s.center(20,'z')
'zzzzhello worldzzzzz'
>>  print('hello\thi')
hello	hi
>>  'hello\thi'.expandtabs()
'hello   hi'
>>  s.isalnum()
False
>>  s.isalpha()
False
>>  s
'hello world'
>>  s.isalpha()
False
>>  'hello'.isalpha()
True
>>  'hello'.isalnum()
True
>>  s.islower()
True
>>  s.isspace()
False
>>  s.istitle()
False
>>  s.endswith('d')
True
>>  s[-1]=='d'
True
>>  s.split('e')
['h', 'llo world']
>>  s.partition('i')
('hello world', '', '')
```
### Set
```
>>  s=set()
>>  s.add(1)
>>  s.add(2)
>>  s.add(1)
>>  s
{1, 2}
>>  s.clear()
>>  s
set()
>>  s={1,2,3}
>>  sc=s.copy()
>>  s.add(4)
>>  sc
{1, 2, 3}
>>  s
{1, 2, 3, 4}
>>  s.difference(sc)
{4}
>>  s.difference_update(sc)
>>  s1={1,2,3}
>>  s2={1,4,5}
>>  s1.difference_update(s2)
>>  s2
{1, 4, 5}
>>  s1
{2, 3}
>>  sc
{1, 2, 3}
>>  sc.discard(2)
??  sc
{1, 3}
>>  s1.intersection(s2)
set()
>>  s1
{2, 3}
>>  s2
{1, 4, 5}
>>  s1.add(1)
>>  s1.intersection(s2)
{1}
>>  s1.intersection_update(s2)
>>  s1
{1}
>>  s1={1,2}
>>  s2={1,2,4}
>>  s3={5}
>>  s1.isdisjoint(s2) #they have intersection show return false
False
>>  s1.isdisjoint(s3)
True
>>  s1
{1, 2}
>>  s2
{1, 2, 4}
>>  s1.issubset(s2)
True
>>  s2.issuperset(s1)
True
```

### dictionary
```
>>  d={'k1':1,'k2':2}
>>  {x: x**2 for x in range(10)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>  {k: v**2 for k,v in zip(['a','b'],range(10))}
{'a': 0, 'b': 1}
>>  for i in d.items():
    print(i)
('k1', 1)
('k2', 2)
>>  for i in d.keys():
    print(i)    
k1
k2
>>  for i in d.values():
    print(i)  
1
2
>>  d.items()
dict_items([('k1', 1), ('k2', 2)])
>>  d.values()
dict_values([1, 2])
>>  d.keys()
dict_keys(['k1', 'k2'])
>> from collections import Counter
>>  res='hello world'
>>  res=dict(Counter(res))
>>  max(res,key=res.get)

```
### abs
```
>>  abs(-2)
2
```
### list
```
>>  l=[1,2,3]
>>  l.append(4)
>>  l.count(1)
1
>>  l1=[5,6]
>>  l.append(l1)
>>  l
[1, 2, 3, 4, [5, 6]]
>>  l.pop()
[5, 6]
>>  l
[1, 2, 3, 4]
>>  l1
[5, 6]
>>  l.extend(l1)
>>  l
[1, 2, 3, 4, 5, 6]
>>  l.append(5)
>>  l.remove(5)
>>  l
[1, 2, 3, 4, 6, 5]
>>  l.index(3)
2
>>  del l[2]
>>  l
[1, 2, 4, 6, 5]
>>  l.insert(2,3)
>>  l
[1, 2, 3, 4, 6, 5]
>>  l.reverse()
>>  l
[5, 6, 4, 3, 2, 1]
>>  l.sort()
>>  l
[1, 2, 3, 4, 5, 6]

```
