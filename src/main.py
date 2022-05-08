"""
Author: arcsi1989
"""
import os
from pathlib import Path
from typing import Dict
import json

import gzip
import shutil
import requests

from pyspark import SparkContext, SparkConf


def combine_part_counts(path: str, file_start: str) -> Dict:
    """
    Fuse the individually created files and their word count content (part-XXXXX) into a single dictionary

    Args:
        path (str): A string containing the path to the created word count files
        file_start (str): A string defining how the created files are started (e.g. 'part')

    Returns:
        word_occurences(dict): A dictionary in which the keys are the identified words in the text and the values are
                               corresponding word occurences
    """
    files = [name for name in os.listdir(path) if os.path.isfile(path + '/' + name) and name.startswith(file_start)]

    word_occurences = dict()
    for file in files:
        file_to_read = open(path + '/' + file, 'r')
        while True:
            # Get next line from file
            line = file_to_read.readline()
            line = line[2:]
            line = line[:-2]
            occurence = line.rsplit(',', 1)[-1]
            word = line[:-(len(occurence) + 2)]
            if len(word) > 0:
                if word is word_occurences.keys():
                    word_occurences[word] += int(occurence)
                else:
                    word_occurences[word] = int(occurence)

            # if line is empty
            # end of file is reached
            if not line:
                break
            # print("Line{}: {}".format(count, word))

        file_to_read.close()

    return word_occurences


def word_counter():
    """Counts the occurence of words from a text downloaded from a provide URL"""
    print('LOG | Assessment whether the code is running inside ')
    if os.getenv('DOCKER_running'):
        path = "/usr/src/data"
    else:
        path = 1
        raise ValueError(f"The provided path does not exist: {path}")

    print('LOG | Word Counter is initiated')

    # Pull the data from the S3 bucket
    print('LOG | Downloading compressed file from provided URL')

    url = os.getenv('DATA_URL')
    compressed_file_name = Path(url).name
    file_name = compressed_file_name[:-len(Path(url).suffix)]
    response = requests.get(url)

    open(f"/usr/src/data/{compressed_file_name}", "wb").write(response.content)

    print('LOG | Extracting downloaded compressed file')
    with gzip.open(f"/usr/src/data/{compressed_file_name}", 'rb') as f_in:
        with open(f"/usr/src/data/{file_name}", 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    # Create Spark context with necessary configuration
    sc = SparkContext("local", "PySpark Word Counter")

    # Read data from everyline of text file starting with 'BG:'  and split each line into words
    print('LOG | Reading provided file')
    words = sc.textFile(f"/usr/src/data/{file_name}").flatMap(
        lambda line: line.split(" ") if line.startswith("BG:") else [])

    # Count the occurrence of each word
    print('LOG | Counting occurence of each word')
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

    # Save the counts to output folder
    print('LOG | Save the counts to output')
    wordCounts.saveAsTextFile("/usr/src/data/output/")

    print('LOG | Fuse the counts and save')
    json_object = json.dumps(combine_part_counts(), indent=4)
    with open("/usr/src/data/results/word_count.json", "w") as outfile:
        json.dump(combine_part_counts(path='/usr/src/data/output', file_start='part'), outfile)


if __name__ == '__main__':
    word_counter()
