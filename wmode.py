def write_file_header():
    file_name = input("Enter the file name: ")
    header = input("Enter the header: ")
    try:
        with open(file_name, 'w') as file:
            file.write(header + "\n")
        print("Header written to file successfully.")
    except IOError:
        print("Error writing to file. Please check the file name and try again.")

write_file_header()