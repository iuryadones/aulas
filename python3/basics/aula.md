---
title    : Python Easy
author   : Prof. Iury Adones
output   : 
    revealjs::revealjs_presentation
---

# Python

---

##  O que é Python?

  * Python é uma linguagem de programação de alto nível
  * Python é interpretada
    + de script
    + imperativa
    + orientada a objetos
    + funcional
    + de tipagem dinâmica e forte

---

## História

### Linguagem **Python**
 * Foi lançada por *Guido van Rossum* em 1991
 * Atualmente o desenvolvimento é aberto (*open-source*)
 * Gerenciado pela organização sem fins lucrativos **Python Software
   Foundation**

---

## Lançada pela comunidade python

### Versão estável 
Python 3.7.x

---

## Estilo de tipagem
  * Dinâmica
  * Forte

---

## Python é uma linguagem multiparadigma
  * Programação Orientação a Objetos
  * Programação Imperativa
  * Programação Funcional

---

## Referência

  * [wikipedia.org/Python](https://pt.wikipedia.org/wiki/Python
"wikipedia sobre Python")

# Download and Install

---

## Instalando Python 3.7 no Windows

### Download 
site: [python.org](https://www.python.org "Python")

---

## Instalando no Ubuntu

### Abra o terminal
shortcut: `ctrl + alt + t`

Digite

```{.bash }
sudo apt-get install python3
```

---

## Instalando no Archlinux

### Abra o terminal

Digite

```bash
sudo pacman -S python
```

# Executar Python

---

### Windows
Pesquise por **`prompt de commandos`**, mas também conhecido como **`cmd`**

### Linux e Mac
Pesquise por **`terminal`**

---

## Sobre `terminal` e `prompt`

O **`terminal`** e **`prompt`** são usados para gerenciar o sistema operacional e
ambiente de desenvolvimento.

Podemos enviar linhas de commandos que serão interpretadas e executadas. 

Interpretadores de comandos são chamados de **`shell`**.

---

## Checar a versão do python

### Digite a linha de comando, depois pressione a teclar **`Enter`**
```bash
python --version
```

```
Python 3.7.x
```

---

## Vamos iniciar o `shell` do python

### **`Terminal`** ou **`prompt`**
```bash
python
```

```
Python 3.7.x (default, May ## ####, ##:##:##) 
[GCC #.#.# ########] on linux
Type "help", "copyright", "credits" or "license" ...
>>> 2 + 2 
4
>>>
```

---

## Como identificar se estamos no shell do python?

Na linha de comando de python tem **`>>>`**

---

## Imprime o ``hello world''

### Shell do Python
```python
>>> print('Olá mundo!')
Olá mundo!
>>> exit()
```

---

## Por que no comando **`exit`** colocar `(` `)`?
 
  * Linguagem de programação é puramente linguagem matemática
    + $f(x) = x^2$
      - $f(x=0) = 0$
      - $f(1) = 1$
      - $f(2) = 4$
      - $f(3) = 9$
    + `exit()` -> A função envia uma mensagem ao sistema operacional que deseja 
    sair do shell do python

# Python tipos de variáveis

---

## Interger 

### `int()`
```python
0
1
-53
22
100
```

---

## Float 

### `float()`
```python
0.0
1.2
-34.44
234.23
3e3
5E4
6e-10
2E-10
```

---

## Complex

### `complex()` 
```python
(1+2j)
(0j)
(5+3j)
(1-2j)
```

---

## String

### `str()`
```python
"Olá mundo"
"1º lugar"
'Preço 3.56'
'A festa foi "divertida"'
```

---

## List

### `list()`
```python
[1, 2, 3, 4, 5]
['maçã', 'banana']
[1, 'maçã', 2, 'banana']
```

---

## Dicionary

### `dict()`
```python
{'cpf': '094.940.490-04'}
{'001': {'nome': 'Usuário de Python', 'idade': 22}}
{'x': 10, 'y': 3}
```

---

## Set

### `set()`
```python
{'maçã', 'uva', 'queijo'}
{1, 2, 3, 4}
{[1,2,3],'maçã'}
```

---

## Boolean

### `bool()`

```python
True
False
```

---

## Empty

### `NoneType`
```python
None
```

# Python Básico

---

## Python Básico 

### Tipagem dinâmica
```python
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

## Python Básico 

### Tipagem dinâmica
```python 
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

## Python Básico

### Input de variáveis
```python
>>> valor_in = input("Digite um valor: ")
Digite um valor: 10
>>> type(valor_in)
<class 'str'>
>>> valor_in
'10'
>>> valor_in = int(valor_in)
>>> type(valor_in)
<class 'int'>
>>> valor_in
10
>>> 
```

---

## Python Básico 

> Extensão do arquivo em python é **`.py`**

---

## Python Básico 

### Script com python
```bash
touch programa-init.py
echo "print('Ola mundo')" >> programa-init.py
python programa-init.py
```

```
Ola mundo
```

---

## Python Básico 

### Script com python
```bash
echo "print('Ola novamente')" > programa-other.py
python programa-other.py
```

```
Ola novamente
```

---

## Python Básico 

### Operações básicas da matemática

:::::::::::::: {.columns}
::: {.column width="40%"}

**Operação**

Adição

Subtração

Multiplicação

Divisão

:::
::: {.column width="40%"}

**Operador**

`+`

`-`

`*`

`\`

:::
::::::::::::::

---

## Python Básico

### Operações básicas da matemática

:::::::::::::: {.columns}
::: {.column width="40%"}

**Operação**

Exponenciação

Parte inteira

Módulo

:::
::: {.column width="40%"}

**Operador**

`**`

`//`

`%`

:::
::::::::::::::

---

## Python Básico

### Crie um arquivo chamado `mult.py`
```python
# coding: utf-8 
"""
calcule: f(x,y) = x*y
Sabemos que x e y pertencem aos números Naturais.
"""

x = input("x: ")
y = input("y: ")

x, y = int(x), int(y)

result = x * y

print('x: %d, y: %f' %(x,y))
print('Resultado: %i' %result)
```

---

## Python Básico

### 1 - Forma de imprimir na tela
```python
print(f'x: {}, y: {}'.format(x, y))
print(f'Resultado: {}'.format(result))
```

---

## Python Básico

### 2 - Forma de imprimir na tela
```python
print(f'x: {1}, y: {0}'.format(y, x))
print(f'Resultado: {0}'.format(result))
```

---

## Python Básico

### 3 - Forma de imprimir na tela
```python
print(f'x: {_x}, y: {_y}'.format(_y=y, _x=x))
print(f'Resultado: {r}'.format(r=result))
```

---

## Python Básico

### 4 - Forma de imprimir na tela
```python
print(f'x: {x}, y: {y}')
print(f'Resultado: {result}')
```

---

## Python Básico

### 5 - Forma de imprimir na tela
```python
print(f'x: {x}, y: {y}')
print(f'Resultado: {x * y}')
```

---

## Python Básico

### Exercício

Faça um Programa que peça um número e então mostre a mensagem.

**O número informado foi [número]**

---

## Python Básico

### Exercício

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

---

## Python Básico

### Exercício

Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre
a temperatura em graus Celsius.

$C = \frac{5(F - 32)}{9}$

---

## Python Básico 

### Listas `[]`
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

## Python Básico 

### É legal mexer com listas

```python
liguagem = "python"
caracter = list(liguagem)
print(caracter)

palavra = "".join(caracter)
print(palavra)
```

---

## Python Básico 

### Lista é mutável

```python
matrix = [0]
matrix = matrix*3
print(matrix)
matrix[1] = 2
print(matrix)
```

---

## Python Básico 

### About `list()`
```python
>>> help(list)
```
```python
>>> dir(list)
```

---

## Python Básico 

### Dicionários `dict()`

```python
dic = {'lang': "python"}
print(dic['lang'])

dic["lib"] = 'django'
print(dic)

print("{}\n".format(dic.keys()))
print("%s\n" %dic.values())
```

---

## Python Básico 

### About `dict()`
```python
>>> help(dict)
```
```python
>>> dir(dict)
```

---

## Python Básico 

### Tuplas `tuple()`
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

## Python Básico 

### About `tuple()`
```python
>>> help(tuple)
```
```python
>>> dir(tuple)
```

---

## Python Básico 

### Conjuntos `set()` 
```bash
>>> set([1,2,3,3,2,1])
{1, 2, 3}
>>> s = {1, 2, 3}
>>> s.union({2,3,5})
{1, 2, 3, 5}
```

---

## Python Básico 

### About `set()`
```python
>>> help(set)
```
```python
>>> dir(set)
```

---

## Estrutura de controle

### Delimitado por indentação
```python
a = 0
print("O valor de a é ")
if a == 0:
    print "zero"
else:
    print a
```

  * 4 espaços representa uma indentação.
  * O bloco da indetação é inicializado por **`:`**

---

## Estrutura de controle

  * `if`
  * `elif`
  * `else`
  * `for-else`
  * `while-else`
  * `and`
  * `or`
  * `is`
  * `not`
  * `==`
  * `!=`
  * `<=`
  * `>=`
  * `<`
  * `>`

---

## Repetições

  * `for`
  * `while`
  * `iter`
  * `compreension`

---

## Arquivos

  * `open()`
    + `read()`
    + `write()`
    + `close()`
  * `with`
    + `open()`
    + `read()`
    + `write()`

---

## Módulos padrões `builtins`

  * Zen python
    + `this`
  * `builtins`
  * `sys`
    + módulos
  * `math`
  * `os`
  * `glob`
  * `pathlib`
  * `pickle`
  * `json`

---

## Funções

  * `def`
  * `async def`

---

## Módulos e Pacotes

  * Criação de módulos
  * Usar módulos de terceiros 

---

## Classes

  * `class`
  * `__init__`
  * `__magic__`

---

## Python funcional

  * `lambda`
  * `map`
  * `reduce`
  * `filter`
  * `compreension`
  * `return values of if-else`
  * `return values of or`
