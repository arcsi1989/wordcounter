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

2. Run the application using a provided CLI interface
```shell
wordcounter$ source config/code.env
wordcounter$ task2 word-counter --output_dir <path_to_output_dir>
``` 
Where the `<path_to_output_dir>` is an existing folder on the local computer

## Building and running a Docker image locally
This requires that you have installed Docker and the docker engine is running.

1. Build the Docker image
```shell
wordcounter$ docker build -t word_counter .
```

2. Run the Docker image
```shell
# local_computer_path = Local computer path which will be mounted to the container to store the output
wordcounter$ docker run --env-file config/code.env -v <local_computer_path>:/usr/src/data word_counter
```
If the image `word_counter` has not been built yet, this will happen automatically.

Both the auto-generated `output` folder as well as the folder `results` will be stored under the provided `<local_computer_path>`,
while the former contains the original output of the PySpark, the later contains the `word_count.json` file


