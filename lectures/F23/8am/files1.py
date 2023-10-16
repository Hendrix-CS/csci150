# File I/O (input/output)
#
# Reading from a file

# 1. Open the file:   file = open(filename, 'r')
# 2. Read from the file:
#    - file.read()  to get everything as one giant string
#    OR
#    - file.readlines() to get a list of lines
# 3. Close the file:   file.close()    (polite)

# Writing to a file
#
# 1. Open the file:   file = open(filename, 'w')   (will create if it does not exist)
# 2. Write to it with   file.write(str)
# 3. file.close()


# Example function to get rid of all the blank lines and comments
# from a Python file.
def remove_comments(input_file_name: str, output_file_name: str):
    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')

    for line in input_file.readlines():
        if line.strip() != '' and line[0] != '#':
            output_file.write(line)

    output_file.close()
    input_file.close()

