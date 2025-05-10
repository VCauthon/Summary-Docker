# Webpage connects to Redis using Docker Compose

In this exercise, you will build on the [previous step](../3-webpage-communicates-with-redis/README.md) by connecting your webpage to a Redis service so that the access counter is stored in Redis and persists across runs.

This time, instead of running individual containers manually, you'll use a `docker-compose` file to orchestrate the entire setup.

## Solution

[Here](./compose.yaml) is the solution uses the following `compose.yaml` to define the services and network.

## Steps to run
1. Navigate to the project directory where your `compose.yaml` file is located.
2. Run the services using Docker Compose:
```bash
docker compose up --build
```
3. Access the webpage at [http://localhost:5000](http://localhost:5000). Each visit or interaction on the links lister should increment a counter stored in Redis.

4. Check the counter in Redis:
Open a terminal inside the Redis container:
```bash
docker exec -it <redis-container-id or name> redis-cli
```
Then run:
```bash
GET count_reddit
```
You should see a number representing the current count of accesses, for example:
```bash
"2"
```
