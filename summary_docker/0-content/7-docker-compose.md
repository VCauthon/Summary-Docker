[__HOME__](../../README.md)

> [< GO BACK](./6-network.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GOTO NEXT >](./8-volumes.md)
---
# Introduction

In this section we will talk about the creation of Docker compose files.

#### The main topics that we will cover are:
- [Initializing containers with several parameters](#initializing-containers-with-several-parameters)
- [Docker compose](#docker-compose)
- [Running docker-compose](#running-docker-compose)

---

## Initializing containers with several parameters

In the summary of [7_network](7_network.md) it is demonstrated how two mongo and mongo-express containers can communicate within a docker network.

However... preparing this environment requires a lot of manual work as we must execute the following:
- Command to create a network
- Initialize mongo container
    - Define the environment variables to create the root user
    - ...
- Initialize mongo-express container
    - Define environment variables to link to mongo
    - ...

Actually, you would have to run all this code:

```bash
docker network create 1_demo

docker run
-d \
--network 1_demo \
--name mongo-db
-e MONGO_INITDB_ROOT_USERNAME=root \
-e MONGO_INITDB_ROOT_PASSWORD=root \
-p 27017:27017 \
mongo

docker run -d \
--name mongo-express
-e ME_CONFIG_OPTIONS_EDITORTHEME="dracula" \
-e ME_CONFIG_MONGODB_SERVER="mongo-db" \
-e ME_CONFIG_BASICAUTH_USERNAME="web" \e ME_CONFIG_BASICAUTH_USERNAME="web" \
-e ME_CONFIG_BASICAUTH_PASSWORD="web" \e ME_CONFIG_BASICAUTH_PASSWORD="web" \
-e ME_CONFIG_MONGODB_ADMINUSERNAME="root" \
-e ME_CONFIG_MONGODB_ADMINPASSWORD="root" \
-p 8081:8081 \
--network 1_demo \
mongo-express
```

These manuals break the IaC philosophy so we defined the docker compose files which allow us to set all this configuration in a single file (which we can reuse when we need it)

--- 

## Docker compose

Basically, docker compose allows to define all the containers that will be raised when calling it and how they will be configured between them, let's try to make this file with the above code.

The file is still a mapping with the original commands, for example.

For the case of mongo:
```bash
docker run
-d \
--network 1_demo \
--name mongo-db
-e MONGO_INITDB_ROOT_USERNAME=root \
-e MONGO_INITDB_ROOT_PASSWORD=root \
-p 27017:27017 \
mongo
```

The following would be included in the docker-compose:
```yaml

version: '3' # Version of docker-compose
services:
    mongo-db: # --name
        image: mongo
        ports: 
            - 27017:27017 # IMPORTANT IN THIS FORMAT OR IT WILL FAIL.
        environment:
            - MONGO_INITDB_ROOT_USERNAME=root
            - MONGO_INITDB_ROOT_PASSWORD=root

```

For the mongo-express case the following would need to be included.

Example case:
```bash
docker run -d \
--name mongo-express
-e ME_CONFIG_OPTIONS_EDITORTHEME=dracula
-e ME_CONFIG_MONGODB_SERVER=mongo-db
-e ME_CONFIG_BASICAUTH_USERNAME=web
-e ME_CONFIG_BASICAUTH_PASSWORD=web
-e ME_CONFIG_MONGODB_ADMINUSERNAME=root \e ME_CONFIG_MONGODB_ADMINUSERNAME=root
-e ME_CONFIG_MONGODB_ADMINPASSWORD=root \
-p 8081:8081 \
--network 1_demo \
mongo-express
```

The following would be included in the docker-compose:
```yaml

version: '3' # Version of docker-compose
services:
    mongo-db:
        image: mongo
        ports: 
            - 27017:27017
        environment:
            - MONGO_INITDB_ROOT_USERNAME=root
            - MONGO_INITDB_ROOT_PASSWORD=root
    mongo-express:
        image: mongo-express
        ports: 
            - 8081:8081
        environment:
            - ME_CONFIG_OPTIONS_EDITORTHEME=dracula
            - ME_CONFIG_MONGODB_SERVER=mongo-db
            - ME_CONFIG_BASICAUTH_USERNAME=web
            - ME_CONFIG_BASICAUTH_PASSWORD=web
            - ME_CONFIG_MONGODB_ADMINUSERNAME=root
            - ME_CONFIG_MONGODB_ADMINPASSWORD=root
```

> IN DOCKER COMPOSE IT IS NOT NECESSARY TO CREATE A NETWORK SINCE DOCKER-COMPOSE ITSELF GENERATES THE NETWORK.

---

## Running docker-compose

Once we have the generated file (we can call it whatever we want) we have to use it together with the `docker-compose` command to create the required containers in it.



If the file is called __docker-compose-node.yaml__ the command executed would be:
- `docker-compose -f docker-compose-node.yaml up`.