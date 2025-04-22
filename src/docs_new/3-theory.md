[__HOME__](../../README.md)

> [<- PREVIOUS CHAPTER](./2-history.md) __|__ [NEXT CHAPTER ->](./4-containers.md)
---


## INDEX:
- 

---

### Differences between VM and Containers

Containers and VMs are both virtualization technologies for running applications. However, the ways they virtualize are very different:

- __VMs__: Virtualize hardware
- __Containers__: Virtualize OS

In the VM model, you power on a server and a hypervisor boots. When the hypervisor boots, it claims all hardware resources such as CPU, RAM, storage, and network adapters. To deploy an app, you ask the hypervisor to create a virtual machine.

It does this by carving up the hardware resources into virtual versions, such as:
- Virtual CPUs
- Virtual Ram

It packages all them into a VM that looks exactly like a physical server. Once you have the VM, you install an OS and then an app.

In the container model, you power on the same server and an OS boots and claims all hardware resources. You then install a container engine such as Docker. To deploy an app you ask Docker to create a container. It does this by carving up OS resources such as process trees and filesystems into virtual versions and then packaging them as a container that looks exactly like a regular OS.

You then tell Docker to run the app in the container.

![image](../docs/static/0_introduction/the_swarm.png)

> VM Tax, one of the biggest problems with the virtual machine model is that you need to install an OS on every VM - every OS consumes CPU, RAM, and storage and take a relative long time to boot. __Containers get around all of this by sharing a single OS on the host they're running on__.

### Docker engine

The Docker Engine is modular and built from many small specialized components pulled from projects such as the OCI, the CNCF, and the Moby project.

At high level, there are two majors parts to the Docker platform:
- __The CLI (client)__: The CLI is the familiar docker command-line tool for deploying and managing containers. It converts simple commands into API request and sends them to the engine.
- __The engine (server)__: Comprises all the service-side components that run and manage containers.

- ![image](../docs/static/0_introduction/cli_engine.png)

From the image, and making more focus on the docker engine we can detect the following components:
- __containerd__: Lifecycle management from all containers created 
- __shim__: Its the process that will report the status of the container created
- __runc__: Interface with the kernel and run the container at low-level runtime

### Communicating with the engine

### Containers

### Images

#### Registry

#### Tagging

#### Layers

### Building images

#### Multi-architecture

#### Multi-staging

---
> [<- PREVIOUS CHAPTER](./2-history.md) __|__ [NEXT CHAPTER ->](./4-containers.md)