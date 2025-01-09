import os
from typing import TextIO


def count_code_line(o_file: TextIO):
    # Handle a single file

    code_line_count: int = 0

    # TODO
    block_comment_count: int = 0
    docstring_count: int = 0

    while line := o_file.readline():
        line = line.lstrip()
        if line.startswith("#"):
            continue

        if len(line) > 0:
            code_line_count += 1

    return code_line_count


def code_counter(path: str):

    # FILE
    if os.path.isfile(path):
        file_basename = os.path.basename(path)
        if not file_basename.endswith(".py"):
            return 0
        with open(path) as o_file:
            return count_code_line(o_file)

        # /rood/a/b/c/file.txt

    # TODO: DIRECTORY
    # sum function
    # recursive function
    # generator expression # list comprehension
    # [i for i in range(10)] # listcomp
    # (i for i in range(10)) # generator expression

    return sum(
        code_counter(os.path.join(dir_path, file))
        for dir_path, _, files in os.walk(path)
        for file in files
    )


# 25