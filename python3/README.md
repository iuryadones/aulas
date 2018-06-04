# Python 3

Curso de Python 3

# Requesitos para o curso
 - Noções básicas do linux

## Install pyenv

### Ubuntu

```bash
$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev
```

```bash
$ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

```bash
$ pyenv update
```

Listando as versões de python

```bash
$ pyenv install --list
```

Instalando versão de python

```bash
$ pyenv install 3.6.4
```

Criando um ambiente de trabalho com python

```bash
$ pyenv virtualenv 3.6.4 ladc
```

Criando pasta de trabalho

```bash
$ mkdir lab
```

Iniciando o ambiente de trabalho

```bash
$ cd lab
$ echo "ladc" > .python-version
```

```bash
$ python -V
Python 3.6.x
```

Adicione também Python 2.7.x

## Fontes

[pyenv-installer](https://github.com/pyenv/pyenv-installer)

[pyenv fixed Common-build-problems](https://github.com/pyenv/pyenv/wiki/Common-build-problems)

