#take user input
user_input = input()

#tokenize each input item on whitespace
user_input = user_input.split()

#strip non-alphanumeric items
user_input = [x.strip(',') for x in user_input]

#print
print(*user_input, sep = "\n")
