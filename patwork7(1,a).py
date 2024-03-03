import datetime

def create_file_with_timestamp():
    # Get the current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Create a file with the current timestamp as its name
    filename = f"file_{current_timestamp}.txt"

    try:
        with open(filename, 'w') as file:
            file.write("This is a text file created at: " + current_timestamp)
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_file_with_timestamp()
