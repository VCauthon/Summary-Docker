# Creating an own database

The objective of the task is to create a redis container called `redis-db`.

In this container a table will be created where to register the clicks made on the links of a web page.

To confirm that it works generate an empty record with a link to google with 0 clicks and confirm its existence through redis-cli.

For example, you would have to see the following:
- google.com > 0 

To install redis-cli use the following link:

```bash
sudo apt-get install redis-tools
```

This database will be used in future exercises.

---

# SOLUTION

Execute the following command to create a redis container:

```bash
docker run -d --name redis-db -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```

Then connect to the redis database using the following command:
```bash
redis-cli
```

> __NOTE__: By default it connects to the localhost with the expected redis port

To create a registry into redis and seen it you can do the following
```bash
$127.0.0.1:6379> SET google.com 0 EX 60
#OK
$127.0.0.1:6379> GET google.com
#"0" 
```