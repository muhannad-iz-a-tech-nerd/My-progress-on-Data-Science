'''
 Think of a data type as a label that tells Python what kind of value something is, so it knows what to do with it.
 In Python, every value is an object, and even a plain integer like 69 is an object.
 There are no "primitive" data types in Python, which means that all data types are objects and have methods that can be called on them.
 Primitive : Basic value types that are stored and handled differently from objects. They are  not objects at all, they are just raw values in the memory.
 When you write something, python automatically creates an object based on the type of the variable (i.e int, str, float, etc..) in the memory and makes the name of the variable a name that points to it.
 Think of a string as a rope or a chain of different individual characters (letters, numbers, symbols) that are connected together. Each character in the string is like a link in the chain, and the entire string is the whole rope or chain. We can access each character of that string or chain individually by using its position in the string, which is called an index.
 Example:
 '''

print('------------------------------')

my_variable = 'Hello, Python!' # This creates a object named 'My_variable' that points to a string in the memory that contains the value 'Hello, Python!'

print(my_variable) # This will print the value of the object that 'my_variable' points to, which is 'Hello, Python!'

print ('-----------------------------')

#To write a longer string across multiple lines, you can use triple quotes (''' or """):
my_long_string = '''This is a long string that spans multiple lines.
It can contain line breaks and other special characters without needing to escape them.'''
print(my_long_string) # This will print the long string with the line break included.

print ('-----------------------------')
#Now, how do we know the length of our string?
#See, when you create a variable containing a string, Python doesn't just store the characters in an object, it writes how many characters are inside that object like a label on a box. When you call len(), Python just reads the label and hands it over to the len() function
#Example:

print("the length of my variable is: " + str(len(my_variable))) # This will print the length of the string 'Hello, Python!', which is 14 characters (including spaces and punctuation).

print ('-----------------------------')