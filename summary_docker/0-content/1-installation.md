[__HOME__](../../README.md)

> [<- PREVIOUS CHAPTER](./0-introduction.md) [NEXT CHAPTER ->](./2-image-repository.md)
---
# Introduction

In this section we will talk about the installation of Docker.

#### The main topics that we will cover are:
- [Components from Dockers](#components-from-dockers)
- [Installing in ubuntu](#installing-in-ubuntu)
- [Installing on windows or mac](#installing-on-windows-or-mac)

---

## Components from Dockers

As a summary there are the following:
- `Docker Engine`: Containerization technology for building and containerizing your applications.
- `Docker CLI client`: CLI to work with dockers.
- `Docker Scout (additional subscription may apply)`: Find and fix vulnerabilities between different containers inside the same container, helping you create a more secure software supply chain.
- `Docker Buildx`: Allows to create docker images.
- `Docker Extensions`: Use third-party tools within Docker Desktop to extend its functionality.
- `Docker Compose`: Allows to run multiple containers.
- `Docker Content Trust`: Send or received containers can be trusted.
- `Kubernetes`: System for managing containerized applications across multiple hosts.
- `Credential Helper`: Native stores to keep Docker credentials safe.

---

## Installing in ubuntu

__Source__: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04#step-3-using-the-docker-command

__Install docker__:

Run the following commands into the terminal to install docker.

```bash
        sudo apt update
        sudo apt install apt-transport-https ca-certificates curl software-properties-common
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
        apt-cache policy docker-ce
        sudo apt install docker-ce
        sudo systemctl status docker
```
The output should be similar to the following, showing that the service is active and running:
```bash
        Output
        ● docker.service - Docker Application Container Engine
            Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
            Active: active (running) since Tue 2020-05-19 17:00:41 UTC; 17s ago
        TriggeredBy: ● docker.socket
            Docs: https://docs.docker.com
        Main PID: 24321 (dockerd)
            Tasks: 8
            Memory: 46.4M
            CGroup: /system.slice/docker.service
                    └─24321 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
```

## Executing the Docker Command Without Sudo (Optional)

By default, the docker command can only be run the root user or by a user in the docker group, which is automatically created during Docker’s installation process.

If you want to avoid typing sudo whenever you run the docker command, add your username to the docker group:
```bash
    sudo usermod -aG docker ${USER}
    su - ${USER}
    groups
```

> __NOTE__: If you need to add a user to the docker group that you’re not logged in as, declare that username explicitly using... ```sudo usermod -aG docker username```

---

## Installing on windows or mac

If the computer that is to run a Docker container is running Windows or Mac it will be necessary to install Docker Desktop. This will include a light version of the Linux kernel on the computer so that the Docker container can run.

You can download docker desktop from the following link:
- https://www.docker.com/products/docker-desktop/

The [next section](https://docs.docker.com/desktop/) goes into more detail about what features docker desktop includes.

---