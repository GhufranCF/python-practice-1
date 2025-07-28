import sys

def read_file(filename):
    """Loading All at once"""
    with open(filename, 'r') as file:
        return file.readlines()

def read_file_gen(filename):
    """Generator to yield lines from a file one at a time."""
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()



def process_log(filename):
    error_count = 0
    line_gen = read_file_gen(filename)
    print("size in MB with generators:", sys.getsizeof(line_gen) / 1e6)

    all_lines = read_file(filename)
    print("size in MB without generator:", sys.getsizeof(all_lines) / 1e6)

    for line in line_gen:
        if "error" in line.lower():
            error_count += 1
    print(f"total error count in {filename} is {error_count}")    

process_log('dummy_log.txt')