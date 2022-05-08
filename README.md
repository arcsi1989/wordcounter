# Word Counter program

This dummy repo downloads a `.txt` file from an url provided through an environment variable `EXAMPLE_URL`.
Author and title of the document are set using `EXAMPLE_AUTHOR` and `EXAMPLE_TITLE`.

## Quick start

Create Docker container using the following command:

1. Install packages
```shell
WordCounter $ docker build -t word_counter .
```

2. Run the docker container
```shell
# url = "https://s3.amazonaws.com/products-42matters/test/biographies.list.gz"
# local_computer_path = Local computer path which will be mounted to the container to store the output
WordCounter$ docker run -e DATA_URL=<url> -v <local_computer_path>:/usr/src/data word_counter
```

## Building and running a Docker image locally
This requires that you have installed Docker and the docker engine is running.

1. Build the Docker image
```shell
WordCounter$ docker build -it word_counter .
```

2. Run the Docker image
```shell
# url = "https://s3.amazonaws.com/products-42matters/test/biographies.list.gz"
# local_computer_path = Local computer path which will be mounted to the container to store the output
WordCounter$ docker run -e DATA_URL=<url> -v <local_computer_path>:/usr/src/data word_counter
```

Or even easier. Configure the environment variables in `docker-compose.yml` and run:
```shell
WordCounter$ docker-compose up
```
If the image `word_counter` has not been built yet, this will happen automatically.

## References

### Docker
* [Getting started with Docker](https://www.docker.com/get-started/)
* [Creating simple Dockerfiles for Python apps](https://hub.docker.com/_/python)
* [Docker Compose](https://docs.docker.com/compose/)