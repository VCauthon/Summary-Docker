[__HOME__](../../README.md)

> [<- PREVIOUS CHAPTER](./4-images.md) [NEXT CHAPTER ->](./6-network.md)
---
# Introduction

In this section we will talk about the debugging of a docker container.

#### The main topics that we will cover are:
- [How do I know what docker is doing?](#how-do-i-know-what-docker-is-doing)
- [Accessing the Container's Shell](#accessing-the-containers-shell)

---

## How do I know what docker is doing?

Docker has the `docker logs {NAME/ID_CONTAINER}` command to list the logs that a docker has produced during its execution.

This may provide you with an error to help guide you to a solution, however, this may not be enough, the logs may not tell you anything, because, as an example, the logs are generated in a TXT file inside the container itself.

This is where we may be interested in entering the terminal of the container itself.

---

## Accessing the Container's Shell

To access there is the command `docker exec -it {NAME/ID_CONTAINER} /bin/bash`.

Before continuing with the explanation, let's clarify the most unknown parts of the command:
- `-it`: Allows you to initialize an interactive terminal with the container:
    - `-i`: Initializes the interactive session.
    - `-t`: Gives a more user-friendly format to the output returned by the container
- `/bin/bash`: Not all terminals have a shell, so specifying this point indicates that we want to access the shell (an alternative command would be `/bin/sh`).

Examples of use cases with the command terminal can be the following:
- View the container environment variables.
- View logs generated from the server itself
- View the configuration of the docker container