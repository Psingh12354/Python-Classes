# first approach
n=123
string=str(n)
string=list(string)
string
['1', '2', '3']
string.reverse()
string
['3', '2', '1']
''.join(string)
'321'
string
['3', '2', '1']
string=''.join(string)
int(string)
321
#second approach
n=123
reverse=0
while n>0:
    a=n%10
    reverse=reverse*10+a
    n//=10

    
reverse
321
