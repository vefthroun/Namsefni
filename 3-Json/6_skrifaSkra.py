import pathlib, logging

file_path = pathlib.Path("hello.txt")

try:
    with file_path.open(mode="w") as file:
        file.write("Hello, World!")
except OSError as error:
    logging.error("Writing to file %s failed due to: %s", file_path, error)


"""
pathlib.Path is a class that represents concrete paths to physical files in your computer. 
Calling .open() on a Path object that points to a physical file opens it just like open() would do. 
So, Path.open() works similarly to open(), but the file path is automatically provided by the Path object you call the method on.

logging
Check for possible issues, such as a missing file, writing and reading access.
"""
