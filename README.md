# Word Counter program

This program (1) downloads a file from an url provided through an environment variable `DATA_URL`, (2) counts the word
occurences in each line of the text starting with `BG:` and stores in `word_count.json` file under the following folder:
`<provided_output_dir>/results/word_count.json`

## Quick start

The following procedure is tested with Python 3.8.0.

Optional: Create a virtual or conda environment and activate it.
1. Install wordcounter package
```shell
wordcounter$ pip install -e .
```

2. Run the application
```shell
wordcounter$ export DATA_URL="https://s3.amazonaws.com/products-42matters/test/biographies.list.gz"
wordcounter$ task2 word-counter --output_dir <path_to_output_dir>
```

## Building and running a Docker image locally
This requires that you have installed Docker and the docker engine is running.

1. Build the Docker image
```shell
wordcounter$ docker build -it word_counter .
```

2. Run the Docker image
```shell
# url = "https://s3.amazonaws.com/products-42matters/test/biographies.list.gz"
# local_computer_path = Local computer path which will be mounted to the container to store the output
wordcounter$ docker run -e DATA_URL=<url> -v <local_computer_path>:/usr/src/data word_counter
```

If the image `word_counter` has not been built yet, this will happen automatically.
