#Task 1: Read a File and Handle Errors

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                print(f"Line {line_num}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    filename = 'sample.txt'
    read_file(filename)

if __name__ == "__main__":
    main()
