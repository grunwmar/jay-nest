# jay-nest/Sojka
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
    for person in person_source:
        name = person.get('name') | Jay(file_obj)["The name is: {name}"]
        print(name)
```
Console output
```
Josef Novak
Hildegarda Grosbaumerhauptgemeindova
Petr Koren
Tomas Marny
Veronika Tumova
Quido Perinar
```
Content of `jay_messages.txt`
 ```
The name is: Josef Novak 
The name is: Hildegarda Grosbaumerhauptgemeindova
The name is: Petr Koren 
The name is: Tomas Marny 
The name is: Veronika Tumova
The name is: Quido Perinar
 ```
