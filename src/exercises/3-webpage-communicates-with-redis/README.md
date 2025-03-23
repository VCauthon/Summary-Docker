
# Webpage can connects with redis

Once you have finished the [previous](../2-generate-a-webpage/README.md) exercise, you must now modify the code so that the counter that registers the accesses to the web pages is registered in a redis service.

Only docker containers can be used for this exercise.

# Solution

The solution can be doing the following:

## Create a network
```bash
docker network create webpage-redis-network
```

## Raise the redis container
```bash
docker run -d -p 6379:6379 --network webpage-redis-network --name redis-db redis/redis-stack:latest
```

## Lift the code from the web page
```bash
cd src
docker build -t webpage-redis .
docker run --name webpage --network webpage-redis-network -p 5000:5000 webpage-redis
```

Once this is done, we will have the whole infrastructure generated. We will be able to confirm that it works if we access the [web page](http://localhost:5000/) and do, for example, increment the reddit counter by 1 and then check in redis if this number has increased.

```bash
redis-cli
127.0.0.1:6379> GET count_reddit
"2"
```

Then if we pull and lift the solution again and access the web page we can confirm that the counter has persisted over time.
