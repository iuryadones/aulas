---
author: Prof. Iury Adones
title: Python easy 
---

# Cronograma

---

1. Python Básico
2. Arquivos
3. Estruturas de controle 
4. Módulos padrões
5. Funções 
6. Módulos e Pacotes 
7. Python funcional

---

### 1.1 - Python Básico 

Python é uma Linguagem interpretada

``` bash
$ python
Python 3.6.2 (default, Jul 20 2017, 03:52:27) 
[GCC 7.1.1 20170630] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> print("Olá Mundo!")
Olá Mundo
```

---

### 1.2 - Tipagem dinâmica

``` bash
>>> a = 1
>>> type(a)
<class 'int'>
>>> a = 'abacaxi'
>>> type(a)
<class 'str'>
>>> a = 1.0
>>> type(a)
<class 'float'>
```

---

### 1.2.1 - Tipagem dinâmica

``` bash
>>> a = [1, 2.2, '23', 'ola', None]
>>> type(a)
<class 'list'>
>>> a = {1,2}
>>> type(a)
<class 'set'>
>>> a = {1:2}
>>> type(a)
<class 'dict'>
```

---

### 1.3 - Script com python

> Extensão python `.py`

```bash
$ touch programa-init.py
$ echo "print('Ola mundo')" >> programa-init.py
$ python programa-init.py
Ola mundo
```

---

### 1.3.1 - Script com python

> Extensão python `.py`

```bash
$ echo "print('Ola novamente')" > programa-other.py
$ python programa-other.py
Ola novamente
```

---

### 1.4 - Delimitado por indentação

```python
a = 0
print("O valor de a é ")
if a == 0:
    print "zero"
else:
    print a
```

---

### 1.5 - Listas [] 

```bash
>>> a = ["A", "C", 1, 2, 5.0]
>>> print(a[0])
"A"
>>> print(len(a))
5
>>> type(a[4])
<class 'float'>
```


---

### 1.5.1 - É legal mexer com listas

```python
liguagem = "python"
caracter = list(liguagem)
print(caracter)

palavra = "".join(caracter)
print(palavra)
```

---

### 1.5.2 - Lista é mutável

```python
matrix = [0]
matrix = matrix*3
print(matrix)
matrix[1] = 2
print(matrix)
```

---

### 1.5.3 - Saiba mais sobre listas 

About list():

* help(list) ou help([])
* dir(list) ou dir([])

---

### 1.6 - Dicionários dict() 

```python
dic = {'lang': "python"}
print(dic['lang'])

dic["lib"] = 'django'
print(dic)

print("{}\n".format(dic.keys()))
print("%s\n" %dic.values())
```

---

### 1.6.1 - Dicionários dict() 

About dict():

* help(dict)
* dir(dict)

---

### 1.7 - Tuplas tuple() 

```bash
>>> 1,2,3
(1, 2, 3)
>>> tuple([1, 2, 3])
(1, 2, 3)
>>> t = tuple([0, 0, 0])
>>> t[1] = 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> 
>>> l = list(t)
>>> print(l)
[0, 0, 0]
>>> l[1] = 2
>>> print(l)
[0, 2, 0]
```

---

### 1.7.1 - Tuplas tuple() 

About tuple():

* help(tuple)
* dir(tuple)

---

### 1.8 - Conjuntos set() 

```bash
>>> set([1,2,3,3,2,1])
{1, 2, 3}
>>> s = {1, 2, 3}
>>> s.union({2,3,5})
{1, 2, 3, 5}
```

---

### 1.8 - set() 

About set():

* help(set)
* dir(set)

---

### Repetições

---

### Estrutura de controle

---

### Arquivos

---

### Módulos padrões

---

### Funções

---

### Módulos e Pacotes

---

### Classes

---

### Python funcional

