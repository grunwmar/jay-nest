# jay-nest: Sojka
for fun, relax, clean mind, excersice...

basic syntax
``` python
name = person.get('name') | Jay()
print(name)
```
```
[🐦» 'Josef Novak' <class 'str'> ]
Josef Novak
```
is the same as
```python
name = person.get('name')
print(name)
```
```
Josef Novak
```
but in first case, the value of `object` is acquired and printed.


The `Jay()`'s message could be expanded by adding square brackets containging template string after Jay's call
```python
name = person.get('name') | Jay()["The name is: {name}"]
```
```
[🐦» The name is: Josef Novak ]
```

The message acquired by `Jay` could be written to file or stream and ten won't be printed.
```python
with open('jay_messages.txt', 'a') as file_obj:
    name = person.get('name') | Jay(file_obj)["The name is: {name}"]
```
```
FILE: jay_messages.txt
-------------------------------------------------------------------------------------------------------
The name is: Josef Novak
```
