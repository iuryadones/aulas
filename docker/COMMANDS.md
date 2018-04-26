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
