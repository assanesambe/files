def read_entire_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

# Example usage
filename = 'file_name.txt'
print(read_entire_file(filename))

def read_first_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = [next(file) for _ in range(n)]
    return ''.join(lines)

# Example usage
filename = 'file_name.txt'
n = 5  # Number of lines to read
print(read_first_n_lines(filename, n))

def read_last_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return ''.join(lines[-n:])

# Example usage
filename = 'file_name.txt'
n = 5  # Number of lines to read
print(read_last_n_lines(filename, n))

def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
    words = content.split()
    return len(words)

# Example usage
filename = 'file_name.txt'
print(f"Number of words: {count_words(filename)}")

def read_last_n_lines_efficient(filename, n):
    with open(filename, 'rb') as file:
        file.seek(0, 2)  # Move to end of file
        end = file.tell()
        buffer = []
        buffer_size = 0
        file.seek(max(end - 1024, 0), 0)  
        while file.tell() < end:
            line = file.readline()
            buffer.append(line.decode('utf-8'))
            buffer_size += len(line)
            if len(buffer) > n:
                buffer.pop(0)  # Keep only the last n lines
        return ''.join(buffer)

# Example usage
filename = 'file_name.txt'
n = 5  # Number of lines to read
print(read_last_n_lines_efficient(filename, n))
