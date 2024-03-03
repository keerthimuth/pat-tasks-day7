def read_file(filename):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of file '{"E:\keerthi PAT file.txt"}':\n")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{"E:\keerthi PAT file.txt"}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage: provide the name of the text file you want to read
    file_to_read = input("Enter the name of the text file to read: ")
    read_file(file_to_read)