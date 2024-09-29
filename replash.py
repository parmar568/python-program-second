def replace_word_in_file(file_name, old_word, new_word):
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
        
        if old_word not in file_content:
            print("The word is not found in the file.")
            return
        
        new_content = file_content.replace(old_word, new_word)
        
        with open(file_name, 'w') as file:
            file.write(new_content)
        
        print("Word replaced successfully.")
    except IOError:
        print("Error reading or writing to file. Please check the file name and try again.")

file_name = input("Enter the file name: ")
old_word = input("Enter the word to be replaced: ")
new_word = input("Enter the new word: ")
replace_word_in_file(file_name, old_word, new_word)