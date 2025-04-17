[__HOME__](../../README.md)

> [<- PREVIOUS CHAPTER](./1-introduction.md) __|__ [NEXT CHAPTER ->](./3-theory.md)
---


## INDEX:
- 

---

### Where docker comes from

### Container-related standards

#### [__The OCI__](https://opencontainers.org/)

Governance council responsible for low-level container-related standards.

Some history about OCI:
- It operates from the Linux Foundation and was founded in the early days of the container ecosystem when some of the people at a company called CoreOS didn't like the way docker was dominating the ecosystem.
- In response, CoreOS created an open standard called [`appc`](https://github.com/appc/spec) that defined specifications for things such as image format and container runtime.
- The `appc` standard did things differently from Docker and put the ecosystem in an awkward position with two competing standards.
- Competition is usually a good thing, competing standards are generally bad, as they generate confusion that slows down user adoption.
- The main figures of `appc` then decided to came together and formed the OCI as a vendor-neutral lightweight council to govern containers standards.

At the time of the writing the OCI maintains three standards called specs:
- [The image-spec](https://github.com/opencontainers/image-spec): Creates and maintains the software shipping container image format spec
- [The runtime-spec](https://github.com/opencontainers/runtime-spec): Develops specifications for standards on Operating System process and application containers
- [The distribution-spec](https://github.com/opencontainers/distribution-spec): Defines an API protocol to facilitate and standardize the distribution of content

#### The CNCF

#### The Moby Project

---
> [<- PREVIOUS CHAPTER](./1-introduction.md) __|__ [NEXT CHAPTER ->](./3-theory.md)