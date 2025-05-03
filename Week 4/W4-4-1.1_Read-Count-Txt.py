with open('C:\\Users\\shiel\\Downloads\\sample_text.txt', 'r') as file:
    text = file.read()
    underscore = text.count("__")
print(underscore)
 