with open('C:\\Users\\shiel\\Downloads\\sample_text.txt', 'r') as file:
    text = file.read()
    underscore = text.count("__")
print(underscore) # Count the number of underscores in the text file
 