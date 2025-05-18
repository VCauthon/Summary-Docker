# Summary-Docker

## Introduction
`Summary-Docker` is a personal journey into the depths of Docker. The project serves both as a learning tool and as a practical guide, evolving over time to cover core Docker topics and hands-on exercises. Whether you're new to Docker or revisiting concepts, this repo offers structured insights and real-world examples.

## Content

### 🧠 Documentation
1. [History](./src/docs/1-history.md): Learn the origins of Docker, how containers evolved, and the key initiatives that helped standardize container technology
2. [Theory](./src/docs/2-theory.md): Understand how Docker works under the hood — from container vs. VM differences to the engine, image layers, registries, and multi-architecture builds
3. [Containers](./src/docs/3-containers.md): Explore how containers run applications, manage processes, restart policies, and how to interact with them during runtime
4. [Docker Images](./src/docs/4-images.md): Master the image lifecycle: containerizing apps, building and pushing images, using Dockerfile keywords, and optimizing with multi-stage builds
5. [Docker Compose](./src/docs/5-compose.md): Discover how to define and run multi-container applications with Docker Compose using YAML configuration and essential commands
6. [Docker Swarm](./src/docs/6-swarm.md): Learn to build, configure, and scale a Swarm cluster with managers and workers, deploy services, ensure high availability, and manage rolling updates
7. [Docker Stack](./src/docs/7-stack.md): Deploy containerized applications declaratively on Docker Swarm using Stack files and Compose syntax — including networking and load balancing
8. [Network](./src/docs/8-network.md): Understand Docker’s networking model, including bridge and overlay networks, the CNM theory, and how Libnetwork and drivers enable container communication

### 🧪 Exercises
- [Create your first docker image](./src/exercises/0-the-first-image/README.md)
- [Create a redis DB with docker](./src/exercises/1-generate-a-redis-instance/README.md)
- [Containerize a Web page](./src/exercises/2-generate-a-webpage/README.md)
- [Add Redis Caching to the Containerized Web page](./src/exercises/3-webpage-communicates-with-redis/README.md)
- [Deploy Web App and Redis Cache Using Docker Compose](./src/exercises/4-compose/README.md)
- [Deploy a Containerized Web App and Redis on a Swarm Cluster via Stack](./src/exercises/5-stack/README.md)

## 📚 Sources
- [Docker Deep Dive by Nigel Poulton](https://www.amazon.es/Docker-Deep-Dive-Nigel-Poulton/dp/1916585256/) - Special thanks
- [TechWorld with Nana - Docker Crash Course for Absolute Beginners](https://www.youtube.com/watch?v=pg19Z8LL06w)
- [TechWorld with Nana - Docker Tutorial for Beginners](https://www.youtube.com/watch?v=3c-iBn73dDE)
- [Official Docker Documentation](https://docs.docker.com/)
- [Wikipedia: OS-level virtualization](https://en.m.wikipedia.org/wiki/OS-level_virtualization)
- [Programacionymas](https://programacionymas.com/blog/docker-diferencia-entrypoint-cmd)
- [Docker Swarm with Virtual Machines using Multipass](https://dev.to/mattdark/docker-swarm-with-virtual-machines-using-multipass-39b0)
