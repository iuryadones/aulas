uname -a

docker pull ubuntu
docker pull base/archlinux

docker container run base/archlinux ls
docker container run base/archlinux ls -l
docker container run base/archlinux echo "Hello world"
docker container run base/archlinux /bin/bash
docker container run -it base/archlinux /bin/bash

uname -a

exit

docker container ls
docker container ls -a

docker container start <CONTAINER ID>
docker container exec <CONTAINER ID> ls

docker container create name-container

docker run name-container

docker image ls

docker volume ls

docker ps -a

docker system prune -a

# Docker examples hello-world


# Docker examples php server
Leia os arquivos de `examples/php_app`.

Execute os seguintes comandos

```
cd examples/php_app
```

```
docker build -t app-php .
```

```
Sending build context to Docker daemon  3.584kB
Step 1/3 : FROM php:7.0-apache
7.0-apache: Pulling from library/php
############: Pull complete 
.
.
.
Digest: sha256:###...
Status: Downloaded newer image for php:7.0-apache
 ---> ############
Step 2/3 : COPY src/ /var/www/html
 ---> ############
Step 3/3 : EXPOSE 80
 ---> Running in ############
Removing intermediate container ############
 ---> ############
Successfully built ############
Successfully tagged app-php:latest
```

Descrição do comando executado
`docker build -t tag-name <root_Dockfile>`

Abra um novo terminal e execute
```
docker run -p 80:80 app-php
```

Coloque no browser:
 - `http://localhost`
 - `http://127.0.0.1`

Podes testar via linha de comando usando o curl, w3m, e entre outros que fazem
requisições ao servidor http.

exemplo via linha de comando.

```
curl http://localhost
```

podemos baixar o index.html usando

```
wget http://localhost
```

modifique o arquivo `php_app/src/index.php`
Altere a String `"Hello World"` -> `"Hello, user"`
salve a modificação e atualize o browser.

Mudou?

Vamos ver o modo dev!
Segue os passos:
primeiro mate o processo `docker run` com `Control + c`

segundo execute o comando e mude o caminho de acordo com o seu PC

```
docker run -p 80:80 -v /home/user/aulas/docker/examples/php\_app/dev-src/:/var/www/html app-php
```

terceiro execute

```
curl http://localhost
```

quarto passo modifique o arquivo `php_app/dev-src/index.php`
Altere a String `"Inprogress"` -> `"Hello, user"`

quinto e último passo execute

```
curl http://localhost
```

agora tens como desenvolver sem ter que ficar matando e levantando máquina.

# Docker example python

