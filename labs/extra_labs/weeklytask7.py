import sys  # Needed to get command line arguments

# Check if a filename was provided
if len(sys.argv) < 2:
    print("Please provide a filename as a command line argument.")
    sys.exit()

# Get the filename from the first argument
filename = sys.argv[1]

try:
    # Open the file and read its contents
    with open(filename, 'r') as file:
        contents = file.read()

    # Count how many times 'e' appears
    count_e = contents.count('e')

    # Print the result
    print("Number of e's in the file:", count_e)

except FileNotFoundError:
    print("File not found:", filename)
