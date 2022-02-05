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
