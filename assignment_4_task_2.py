#Task 2: Write and Append Data to a File
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."

def main():
    filename = 'output.txt'

    # Take user input and write it to the file
    user_input = input("Enter some text: ")
    write_to_file(filename, user_input + "\n")
    print(f"User input written to {filename}.")

    # Append additional data to the file
    additional_data = input("Enter additional text to append: ")
    append_to_file(filename, additional_data + "\n")
    print(f"Additional data appended to {filename}.")

    # Read and display the final content of the file
    final_content = read_file(filename)
    print(f"Final content of {filename}:")
    print(final_content)

if __name__ == "__main__":
    main()
