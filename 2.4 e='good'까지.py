Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''hello world'''
'hello world'

1+1
2
#hi
"""hi"""
'hi'
a = input("a를 입력하세요:")
a를 입력하세요:10
print a
SyntaxError: incomplete input
print('a')
a
print(a)
10
print(a*2)
1010
age=input('age를 입력하세요:')
age를 입력하세요:10
lastname = input('lastname을 입력하세요:')
lastname을 입력하세요:kim
firstname = ('firstname을 입력하세요:')
firstname = input('firstname을 입력하세요:')
firstname을 입력하세요:minjun
print('당신의 이름은', lastname+firstname, '입니다.')
당신의 이름은 kimminjun 입니다.
print('당신의 나이는' , age , '입니다.')
당신의 나이는 10 입니다.
age=10
name= 'kimminjun'
print('1.제 이름은' , name , '입니다. 제 나이는', age, '입니다.)
      
SyntaxError: incomplete input
print('1.제 이름은' , name , '입니다. 제 나이는', age, '입니다.')
      
1.제 이름은 kimminjun 입니다. 제 나이는 10 입니다.
print('2. 제 이름은{}입니다. 제 나이는 {}입니다.'.format(name,age))
      
2. 제 이름은kimminjun입니다. 제 나이는 10입니다.
print("{0}{1}{0}{1}".format(name,age))
      
kimminjun10kimminjun10
print("{0}{1:3f}".format(name,age))
      
kimminjun10.000000
print('3.제 이름은 %s입니다.제 나이는 %d입니다.'%(name,age))
      
3.제 이름은 kimminjun입니다.제 나이는 10입니다.
3.제 이름은 kimminjun입니다.제 나이는 10입니다.
      
SyntaxError: invalid decimal literal
>>> a=10
...       
>>> print('type(10):',type(a))
...       
type(10): <class 'int'>
>>> print('()')
...       
()
>>> a='10'
...       
>>> print(type(a))
...       
<class 'str'>
>>> b=10.1
...       
>>> print('type(10.1):',type(b))
...       
type(10.1): <class 'float'>
>>> c=-1
...       
>>> print('type(-1):',type(c))
...       
type(-1): <class 'int'>
>>> d=true
...       
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    d=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> d= True
...       
>>> print('type(True):',type(d))
...       
type(True): <class 'bool'>
>>> e='good'
...       
>>> print('type(\'good\'):',type(e))
...       
type('good'): <class 'str'>
