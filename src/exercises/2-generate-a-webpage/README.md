
# Basic dummy Webpage 

Create a docker image with a webpage.

This webpage will show a table where in the first column there will be a series of links and in the second column a counter.

The web page will have a JavaScript script to increase the counter number depending on the selected link.

---

# Solution

The image code can be found [here](./src/__init__.py) and is published in the joeyratt repository as joeyratt/webpage.

Through the following command the image can be pulled up:
```bash
docker run -p 5000:5000 joeyratt/webpage:latest
```