```bash
docker-machine ls
NAME        ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER        ERRORS
```

```
docker-machine create --driver=virtualbox manager-1
```

```
docker-machine ls
NAME        ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER        ERRORS
manager-1   -        virtualbox   Running   tcp://192.168.99.101:2376           v18.03.1-ce   
```

```
docker-machine ip manager-1 
192.168.99.101
```

```
docker-machine ssh manager-1
```

```
docker@manager-1:~$ docker swarm init --advertise-addr 192.168.99.101
```

```
Swarm initialized: current node (dxn1zf6l61qsb1josjja83ngz) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join \
    --token SWMTKN-1-5c7d3cckv8rfrfi50tpaljxbnv2hq2jrkb77tkj93gxbnre3js-f2c6cpog7pofgo2sb1c1fz9m6 \
    192.168.99.101:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```

```
docker@manager-1:~$ docker info
```

```
Containers: 2
Running: 0
Paused: 0
Stopped: 2
  ...snip...
Swarm: active
  NodeID: dxn1zf6l61qsb1josjja83ngz
  Is Manager: true
  Managers: 1
  Nodes: 1
  ...snip...
```

```
docker@manager-1:~$ docker node ls
```

```
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
y4i11qd4vk85ae8m9wm66dz6k *   manager-1           Ready               Active              Leader              18.03.1-ce
```

```
docker@manager-1:~$ docker swarm join-token manager
To add a manager to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-5c7d3cckv8rfrfi50tpaljxbnv2hq2jrkb77tkj93gxbnre3js-f2c6cpog7pofgo2sb1c1fz9m6 192.168.99.101:2377
```

```
docker@manager-1:~$ exit
```

```
docker-machine create --driver=virtualbox node-1
```

```
docker-machine ssh node-1
```

```
docker@node-1:~$ docker swarm join \
                 --token SWMTKN-1-5c7d3cckv8rfrfi50tpaljxbnv2hq2jrkb77tkj93gxbnre3js-f2c6cpog7pofgo2sb1c1fz9m6 \
                 192.168.99.101:2377
```

```
docker@node-1:~$ exit
```

```
docker-machine create --driver=virtualbox node-2
```

```
docker-machine ssh node-2
```

```

docker@node-2:~$ docker swarm join \
                 --token SWMTKN-1-5c7d3cckv8rfrfi50tpaljxbnv2hq2jrkb77tkj93gxbnre3js-f2c6cpog7pofgo2sb1c1fz9m6 \
                 192.168.99.101:2377
```

```
docker@node-2:~$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
y4i11qd4vk85ae8m9wm66dz6k     manager-1           Ready               Active              Leader              18.03.1-ce
rcm6s177a9x5450zmuc7qd3rt     node-1              Ready               Active              Reachable           18.03.1-ce
vz8k9qqmmed0vx7jblwxcz9cu *   node-2              Ready               Active              Reachable           18.03.1-ce
```

```
docker@node-2:~$ exit
```

```
docker-machine shh manager-1
```

```
docker@manager-1:~$ docker service create --replicas 1 --name helloworld alpine ping docker.com
```

```
w8dtfpev6fp7z1royy5zlwub4
overall progress: 1 out of 1 tasks 
1/1: running   [==================================================>] 
verify: Service converged 
```

```
docker@manager-1:~$ docker service ls
```

```
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
w8dtfpev6fp7        helloworld          replicated          1/1                 alpine:latest       
```

```
docker@manager-1:~$ docker service inspect --pretty helloworld
```

```
ID:		w8dtfpev6fp7z1royy5zlwub4
Name:		helloworld
Service Mode:	Replicated
 Replicas:	1
Placement:
UpdateConfig:
 Parallelism:	1
 On failure:	pause
 Monitoring Period: 5s
 Max failure ratio: 0
 Update order:      stop-first
RollbackConfig:
 Parallelism:	1
 On failure:	pause
 Monitoring Period: 5s
 Max failure ratio: 0
 Rollback order:    stop-first
ContainerSpec:
 Image:		alpine:latest@sha256:7df6db5aa61ae9480f52f0b3a06a140ab98d427f86d8d5de0bedab9b8df6b1c0
 Args:		ping docker.com 
Resources:
Endpoint Mode:	vip
```

```
docker@manager-1:~$ docker service inspect helloworld
```

```
[
    {
        "ID": "w8dtfpev6fp7z1royy5zlwub4",
        "Version": {
            "Index": 23
        },
        "CreatedAt": "2018-05-02T16:56:14.558627105Z",
        "UpdatedAt": "2018-05-02T16:56:14.558627105Z",
        "Spec": {
            "Name": "helloworld",
            "Labels": {},
            "TaskTemplate": {
                "ContainerSpec": {
                    "Image": "alpine:latest@sha256:7df6db5aa61ae9480f52f0b3a06a140ab98d427f86d8d5de0bedab9b8df6b1c0",
                    "Args": [
                        "ping",
                        "docker.com"
                    ],
                    "StopGracePeriod": 10000000000,
                    "DNSConfig": {},
                    "Isolation": "default"
                },
                "Resources": {
                    "Limits": {},
                    "Reservations": {}
                },
                "RestartPolicy": {
                    "Condition": "any",
                    "Delay": 5000000000,
                    "MaxAttempts": 0
                },
                "Placement": {
                    "Platforms": [
                        {
                            "Architecture": "amd64",
                            "OS": "linux"
                        },
                        {
                            "OS": "linux"
                        },
                        {
                            "Architecture": "arm64",
                            "OS": "linux"
                        },
                        {
                            "Architecture": "386",
                            "OS": "linux"
                        },
                        {
                            "Architecture": "ppc64le",
                            "OS": "linux"
                        },
                        {
                            "Architecture": "s390x",
                            "OS": "linux"
                        }
                    ]
                },
                "ForceUpdate": 0,
                "Runtime": "container"
            },
            "Mode": {
                "Replicated": {
                    "Replicas": 1
                }
            },
            "UpdateConfig": {
                "Parallelism": 1,
                "FailureAction": "pause",
                "Monitor": 5000000000,
                "MaxFailureRatio": 0,
                "Order": "stop-first"
            },
            "RollbackConfig": {
                "Parallelism": 1,
                "FailureAction": "pause",
                "Monitor": 5000000000,
                "MaxFailureRatio": 0,
                "Order": "stop-first"
            },
            "EndpointSpec": {
                "Mode": "vip"
            }
        },
        "Endpoint": {
            "Spec": {}
        }
    }
]
```

```
docker@manager-1:~$ docker service ps helloworld
```

```
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE            ERROR               PORTS
9vd7zfnaffh2        helloworld.1        alpine:latest       node-1              Running             Running 30 minutes ago                       
```

```
docker@manager-1:~$ exit
```

```
docker-machine ssh node-1
```

```
docker@node-1:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
ae047bccc667        alpine:latest       "ping docker.com"   31 minutes ago      Up 31 minutes                           helloworld.1.9vd7zfnaffh2d0d3caukhr8xb
```

```
docker@node-1:~$ exit
```

➜  cluster_swarm git:(master) ✗ docker-machine ssh manager-1 
                        ##         .
                  ## ## ##        ==
               ## ## ## ## ##    ===
           /"""""""""""""""""\___/ ===
      ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
           \______ o           __/
             \    \         __/
              \____\_______/
docker@manager-1:~$ docker service scale helloworld=5
helloworld scaled to 5
overall progress: 5 out of 5 tasks 
1/5: running   [==================================================>] 
2/5: running   [==================================================>] 
3/5: running   [==================================================>] 
4/5: running   [==================================================>] 
5/5: running   [==================================================>] 
verify: Service converged 
docker@manager-1:~$ docker service ps helloworld
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE            ERROR               PORTS
9vd7zfnaffh2        helloworld.1        alpine:latest       node-1              Running             Running 34 minutes ago                       
xu43xp6u87gl        helloworld.2        alpine:latest       manager-1           Running             Running 18 seconds ago                       
sbf2mklmtwla        helloworld.3        alpine:latest       node-1              Running             Running 24 seconds ago                       
7h423am7ym3e        helloworld.4        alpine:latest       node-2              Running             Running 17 seconds ago                       
gaqzbwpdrur5        helloworld.5        alpine:latest       manager-1           Running             Running 18 seconds ago                       
docker@manager-1:~$ 
