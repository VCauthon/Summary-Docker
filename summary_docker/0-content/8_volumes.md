[HOME](../README.md)

> [< GO BACK](./7_docker_compose.md)
---

# Introduction

In this section we will talk about the creation of Docker volumes.

#### The main topics that we will cover are:
- [Docker volumes](#docker-volumes)
- [Docker types](#docker-types)
- [Path to the volumes](#path-to-the-volumes)

---

## Docker volumes

Containers do not have data persistence, that is, every time a container is lifted it starts without any data and all the data generated during the life of the container will be deleted once the container is stopped or deleted.

Therefore, docker offers the concept of volumes to link a volume from the current host to the container. This allows everything that docker generates on that volume to be stored forever on disk in the memory space that is allocating that volume.

---

## Docker types

The volume mentioned above corresponds to a specific type of volume, as there are many of them. 

It is specified when running the `docker run ...` with the `-v` parameter or in the `docker-compose` itself in a parameter called `volumes`.

The volume types that exist are as follows:
- __Host volumes__:
    - The data volume is located on the computer itself.
    - `... -v {PATH LOCAL HOST}:{PATH INSIDE CONTAINER}`: The data volume is located on the machine itself.
    - `... -v /home/mount/data:/var/lib/mysql/data`...
- __Anonymous volumes__:
    - Docker takes care of creating a volume automatically and randomly.
    - `... -v {PATH INSIDE CONTAINER}`
    - `... -v /var/lib/mysql/data`...
- __Named volumnes__:
    - This is a mix of the two types of volumes as it allows the volume to be named and is generated automatically
    - `... -v {NAME VOLUME REFERENCE VOLUME PATH}:{PATH INSIDE CONTAINER}`.

The most recommended volume type is named volumes.

---

## Path to the volumes

- Windows: C:\ProgramData\docker\volumes
- Linux: /var/lib/docker/volumes
- Apple: /var/lib/docker/volumes