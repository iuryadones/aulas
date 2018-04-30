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

Leia os arquivos de `examples/first_app`.

Execute os seguintes comandos

```
cd examples/first_app
```

```
docker build -t hello-world .
```

```
Sending build context to Docker daemon  3.072kB
Step 1/5 : FROM python:3
3: Pulling from library/python
############: Pull complete 
.
.
.
Digest: sha256:###...
Status: Downloaded newer image for python:3
 ---> ############
Step 2/5 : RUN mkdir -p /usr/src/app
 ---> Running in 118cccad6ee7
Removing intermediate container 118cccad6ee7
 ---> ############
Step 3/5 : WORKDIR /usr/src/app
Removing intermediate container ############
 ---> ############
Step 4/5 : COPY . .
 ---> ############
Step 5/5 : CMD [ "python", "./hello_world.py" ]
 ---> Running in ############
Removing intermediate container ############
 ---> ############
Successfully built ############
Successfully tagged hello-world:latest
```

Execute o container

```
docker run hello-world 
```

Resposta da execução

```
Hello World
```

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
docker run -p 80:80 -v /home/user/aulas/docker/examples/php_app/dev-src/:/var/www/html app-php
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

# Docker compose example python

Leia os arquivos de `examples/micro_service`.

Execute os seguintes comandos

```
cd examples/micro_service
```

`TODO: tree dir`

Exite o product/Dockerfile, mas não precisamos usar o `docker build` e `docker run`.

Execute o comando no `examples/micro_service`, temos neste diretório o arquivo
`docker-compose.yml` que já têm as instruções do container.


```
docker-compose up
```

Entre no link [http://localhost:5001](http://localhost:5001)

A exibição de um json

```
{
    "product": [
        "Ice cream",
        "Chocolate",
        "Fruit"
    ]
}
```

agora criar um novo micro-service para o website usando php

```bash
mkdir examples/micro_service/website
cd examples/micro_service/website
```

Crie um arquivo `index.php` dentro da pasta `website`.

```bash
touch index.php
```

copie o conteudo

```php
<html>
    <head>
        <title>Loja de Sweets</title>
    </head>
    <body>
        <h1>Sejam bem vindos!</h1>
        <ul>
            <?php
                $json = file_get_contents('http://product-service');
                $obj = json_decode($json);

                $products = $obj->products;
                foreach ($products as $product) {
                    echo "<li>$product</li>";
                }
            ?>
        </ul>
    </body>
</html>
```

Modifique o arquivo `docker-compose.yml`:
 - Add um novo serviço de website, primeiro temos a imagem do `php:apache`
 - Add `volumes` de desenvolvimento
 - Add `ports` do website
 - Add `depends_on` do `product-service`

```yaml
version: '3'

services:
    product-service:
        build: ./product
        volumes:
            - ./product:/usr/src/app
        ports:
            - 5001:80

    website:
        image: php:apache
        volumes:
            - ./website:/var/www/html
        ports:
            - 5000:80
        depends_on:
            - product-service
```

Entre no link [http://localhost:5000](http://localhost:5000)

podemos subir a máquina e deixar em background, assim podemos usar livremente o
terminal.

execute assim

```bash
docker-compose up -d
```

para derrubar as maquinas precisaremos executar a seguinte linha de comando

```bash
docker-compose down
```
