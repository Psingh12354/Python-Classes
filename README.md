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
