# Print statement or function
print ("hello, world")

# Input function
# name here is a variable
# Ask user for a name and print it with a hello
name = input("What is your name? ")
print ("hello,", name)

# Python docs: https://docs.python.org/3/library/functions.html
# To erase the newline after the print statement, use end="".
print ("Hello, ", end="")
print ("world")

# Using f-strings, strip and title methods
name = input("What is your name? ").strip().title() 
print (f"hello, {name}")

#Use split method to split a string into a list of words
first, last = name.split(" ") # Strings will be split by a space
print (f"hello, {first}")