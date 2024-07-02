class color:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

name = input("Please enter your name: ")
age = input("Please enter your age: ")

underlined_name = color.UNDERLINE + name + color.END

output = color.BOLD + "Name" + color.END + ": " + underlined_name + ", " + color.BOLD + "Age" + color.END + ": " + age 

print(output)
