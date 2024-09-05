

File :
Approach-1
------------------------
>>> f = open('chai.py')
>>> f.readline()
'import time\n'# >>> f.readline()
'print("chai is here")\n'
>>> f.readline()
'username = "hitesh"\n'
>>> f.readline()
'print(username)'
>>> f.readline()
''
Approach-2
------------------
>>> f.readline()
'print(username)'
>>> f.readline()
''
>>> f.readline()
''
>>> f.readline()
'print(username)'
>>> f.readline()
''
>>> f.readline()
>>> f.readline()
'print(username)'
>>> f.readline()
>>> f.readline()
'print(username)'
'print(username)'
>>> f.readline()
''
>>> f.readline()
''
>>> f = open('chai.py')
>>> f.__next__()
'import time\n'
>>> f.__next__()
'print("chai is here")\n'
>>> f.__next__()
'username = "hitesh"\n'
>>> f.__next__()
'print(username)\n'
>>> f.__next__()
'\n'
>>> f.__next__()
>>> f.__next__()
>>> f.__next__()
'#File :\n'
>>> f.__next__()
>>> f.__next__()
>>> f.__next__()
>>> f.__next__()
'#File :\n'
>>> f.__next__()
'#------------------------\n'

Approach-3
---------------------------------
>>> for line  in open('chai.py'):
...   print(line, end='')
...
import time
print("chai is here")
username = "hitesh"
print(username)

Approach-4
---------------------------------
>>> f = open ('chai.py')
>>> while True:
...   line = f.readline()
...   if not line: break
...   print(line, end='')
...
import time
print("chai is here")
username = "hitesh"
print(username)



Approach-4
---------------------------------
>>> test = "hitesh"
>>> if not test:
...   print("chai")
... 
>>> test=""
>>> if not test:
...  print("chai")
... 
chai


1.Iteration tool(for, comprehention)
next()
next()
next()
__next__()     
2.iter()
3.iterable objects (list,file)



  Iterator
---------------
>>> myList=[1,2,3,4]
>>> I = iter(myList)
>>> I
<list_iterator object at 0x000002077E8E9EA0>
>>> I.__next__()
1
>>> I
<list_iterator object at 0x000002077E8E9EA0>
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

>>> f = open('chai.py')
>>> iter(f) is f
True
>>> iter(f) is f.__iter__()
True


>>> D = { 'a':1, 'b':2 }
>>> for key in D :
>>> D = { 'a':1, 'b':2 }
>>> for key in D :
>>> for key in D :
...   print (key)
...   print (key)
...
a
b


>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x000002077E91CC70>
>>> next(I)
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration


>>> range(5)
range(0, 5)
>>> R = range(5)
>>> I = iter(R)
>>> next(I)
0
>>> next(I)
1
>>> 
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIter