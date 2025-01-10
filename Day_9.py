#Concept of Immutability:
#string is immutable, when we add changes in the string it will form a new string
#rstrip removes any trailing characters
#split helps to create a list of the items in a string
#capitalise helps to create all the first char into upper case but converts the rest of the char to lower case

a="Python!! python"
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("python", "java"))
print(a.split(" "))
heading = "introduction to python Basics"
print(heading.capitalize())
print(heading.center(50))
print(heading.endswith("."))
print(heading.find("to"))
print(heading.isalnum())
print(heading.isalpha())
print(heading.islower())
print(heading.isprintable())
print(heading.isspace())