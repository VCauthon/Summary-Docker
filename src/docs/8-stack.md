[__HOME__](../../README.md)

> [<- PREVIOUS CHAPTER](./7-swarm.md) __|__ [NEXT CHAPTER ->](./9.network.md)
---


## INDEX:
- 

---

### Introduction

Docker stacks combine [compose](./6-compose.md) and [swarm](7-swarm.md) to create a platform for easy deployment and management of complex multi-container apps on secure, highly available infrastructure.

You build a swarm, define your apps in Compose file, and deploy and manage them with the docker `stack command`.

From an architecture perspective, __stacks are at the top of the Docker application hierarchy__ - they build on top of services, which in turn build on top of containers, and they only run on swarms.

> __TERMINOLOGY__: Throughout this chapter, we'll use the term service to refer to the Docker service object that manages one or more identical containers on a swarm. We'll also refer to the _Compose_ file as the _stack file_, and sometimes we'll refer to the application as the _stack_.

### Prepare environment

If you already have a swarm you can continue, otherwise visit the following section to know how to create it.

For this section we will work with a cluster with `1 manager` and `2 workers`.

If you have already created the cluster as indicated in the previous chapter you only need to include one more worker.

This can be done with the following commands:
```bash
multipass launch docker --name worker2 --cpus 2 --disk 40G --memory 4G
multipass shell worker2
docker swarm join \
    --token SWMTKN-1-4wlq6le2gs765sio8u8v5lm19b4eekwq72nbk2925111ycat46-6garqnzdhojyzqk30p2l8fkhs 10.222.216.226:2377 \
    --advertise-addr 10.222.216.246:2337 \
    --listen-addr 10.222.216.246:2337
```

> __NOTE__: Take into account that the token provided its the one created by your own manager

Through the `docker node ls` command you can confirm if you already have all the nodes integrated.

Here is an example of what you should see:
```bash
docker node ls
ID                            HOSTNAME   STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
d1nlhrih8a3kmjlef3s22rjrw *   manager1   Ready     Drain          Leader           28.1.1
x8pft1i3vlkdqydu1mpaa04oh     worker1    Ready     Active                          28.1.1
o5eq6iwt2bsnb2iddityjlghy     worker2    Ready     Active                          28.1.1
```

> __NOTE__: Remember that the listing can only be done from the manager

#### Hands on

In this section we will see how we can deploy the solution created in [exercise 4](../exercises/4-compose/README.md), that is, a webapp with a connection to redis to store in memory the actions performed by the user.

##### Looking closer at the stack file

Stack files are identical to Compose files with a fe differences at run-time. For example Docker Compose lets you build images at run-time, but Docker Stack don't.

Let's look at the networking elements defined in the [stack file](../exercises/4-compose/compose.yaml).

---
> [<- PREVIOUS CHAPTER](./7-swarm.md) __|__ [NEXT CHAPTER ->](./9.network.md)