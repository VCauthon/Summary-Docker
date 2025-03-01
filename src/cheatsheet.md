# Docker Quick Reference Guide

This document serves as a quick reference guide for common Docker commands and concepts. It is structured to provide a comprehensive overview of Docker's functionality, ranging from basic command line interactions to more advanced features like Docker Compose and Dockerfile instructions.

#### The main topics that we will cover are:
- [Listing current local docker content](#listing-current-local-docker-content)
- [Downloading imagees from Docker](#downloading-images-from-docker)
- [Building images](#building-images)
- [Building containers](#building-containers)
- [Working with containers](#working-with-containers)
- [Dockerfile instructions](#dockerfile-instructions)
- [Docker Compose](#docker-compose)
- [Path to the volumes](#path-to-the-volumes)

---

## Listing current local docker content
- Images
    - `docker images`
- Containers
    - `docker ps`
    - Added features:
        - List all running and stopped containers:
            - `-a`

## Downloading images from Docker:
- Last version
    - `docker pull {NAME_IMG}`
- Concrete version
    - `docker pull {IMG}:{TAG_VERSION}`

## Building images:

- __Creating an image:__
    - `docker build .`
    - Added features:
        - `-t {NAME-IMG}:{VERSION}`: Sets the name and version of the image
- __Deleting:__
    - __Containers:__
        - `docker rm {CONTAINER_ID}`
    - __Images:__
        - `docker rmi {IMAGE_ID}`
        - __NOTE__: The containers from this image have to be deleted before deleting the image

## Building containers:

- Create:
    - Last version
        - `docker run {NAME_IMG}`
    - Concrete version
        - `docker run {IMG}:{TAG_VERSION}`
    - Added features:
    - `-d`: The terminal doesn't show the logs
    - `-v`: Sets the volume used by the container
    - `-p {HOST_PORT}:{HOST_CONTAINER}`: Sets a port binding between the host and the container
    - `--name 'CONTAINER_NAME'`: Give a concrete name to the created container
    - `--network 'NETWORK_NAME`: Creates a container inside a docker network
    - `-it`: Make the container interactive and to attach your shell to the container's terminal.
- Rerun:
    - `docker start {CONTAINER_ID/CONTAINER_NAME}`
- Delete:
    - `docker stop {CONTAINER_ID/CONTAINER_NAME}`

## Working with containers:

- Showing logs:
    - `docker logs {CONTAINER_ID/CONTAINER_NAME}`
    - The container ID can be retrieved from the `docker ps` command
    - 
- Opening a session with a container:
    - `docker exec -it {CONTAINER_ID/CONTAINER_NAME} /bin/bash`
        - `-it`: Creates a terminal with the docker
        - `/bin/bash`: Starts the shell from the container (not all images have a shell!)
- Network:
    - `docker network`
        - `ls`: List all the existing networks
        - `create {NETWORK_NAME}`: Creates a new network

## Dockerfile instructions:

- `FROM`: Specifies the base image from which our Docker image is built.
- `COPY`: Copies files and directories from the build context into the container's filesystem.
- `WORKDIR`: Sets the working directory for commands like `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, and `ADD` in the Dockerfile.
- `RUN`: Executes commands during the image build process, commonly used for installing software.
- `CMD`: Defines the default command that will be executed when a container is started from the image. Only the last `CMD` command will take effect.
- `ENV`: Sets all the container environment variables.

## Docker Compose:

- Commands in shell:
    - `docker-compose up`: Running all the containers of the docker-compose
    - `docker-compose down`: Stops all the containers associated to the docker-compose
        - Features:
            - `-f {file.yaml}`: Concrete the docker-compose file
            - `-d`: Detach mode
- docker-compose.yaml file:
    - `version`: Needed to tell the version used
    - `services`: Sets what will have the concrete service
        - `image`: Docker image used by this service
        - `build`: Uses a dockerfile as image ("needs the ".")
        - `ports`:  Port binding
        - `environment`: Concrete environment variables set in the container
        - `depends_on`: Tells that this services depends on another before starting
        - `volumes`: Sets the type of the volume
- Debugging notes:
    - Checking the path of the container:
        - Add into the services of the docker-compose: `command: ["ls"]`

## Path to the volumes

- **Windows**: C:\ProgramData\docker\volumes
- **Linux**: /var/lib/docker/volumes
- **Apple**: /var/lib/docker/volumes
