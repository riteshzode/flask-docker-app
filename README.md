# Simple Python Flask Dockerized Application#

Build the image using the following command

```bash
$ docker build -t python-docker:latest .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 5000:5000 python-docker:latest
```

# Step by step guide by freecodecamp.org

**https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/**

The application will be accessible at http:127.0.0.1:5000 