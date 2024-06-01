def write_file(file_name, file_content):
    # Open the file in write mode ('w').
    with open(f'{file_name}.txt', 'w') as f:
        # Write the content to the file.
        f.write(file_content)

def append_file(file_name, append_content):
    # Open the file in append mode ('a').
    with open(f'{file_name}.txt', 'a') as f:
        # Append the content to the end of the file.
        f.write(append_content)

def read_file(file_name):
    # Open the file in read mode (default mode when not specified).
    with open(f'{file_name}.txt') as f:
        # Read the entire content of the file.
        return f.read()
