'''Now, there are multiple ways to manipulate strings in Python, and one of the most common ways is through string methods. String methods are built-in functions that can be called on string objects to perform various operations on them. For example, you can use the .upper() method to convert a string to uppercase, or the .lower() method to convert it to lowercase. There are many other string methods available in Python that can help you manipulate strings in different ways. Let's see some examples of string manipulation using string methods:
Example:
'''
my_pleasure = 'Thank you, kind sir!!'

print('-----------------------------')

print(my_pleasure.upper()) # This will print 'THANK YOU!' (converts the string to uppercase)
print(my_pleasure.lower()) # This will print 'thank you!' (converts the

print('-----------------------------')

# Now, let's say that we want to count a certain number of characters in our string
'''For that, we can use the .count() method, which counts the number of occurrences of a specific character or substring in a string. For example, if we want to count how many times the letter 'o' appears in our string, we can do it like this:'''

# print(my_pleasure.count()) 

'''
The code on line 16 is commented out because it raises a TypeError. What's a TypeError, you ask? Let's see.
A TypeError is Python's way of saying: "You gave me the wrong kind of thing."
It shows up when you try to do an operation on a value that's the wrong type for that operation. Python is strict about types — you can't just mix and match however you want.
'''

'''Now, why did did we get a TypeError on line 16 even though we weren't trying to do any mathematical operation or just an operation in general?'''

'''
Great question! The TypeError you saw there has nothing to do with math at all — that was just one *example* of a TypeError.

The name "TypeError" is a bit misleading at first. It doesn't only mean math mistakes. It means, more broadly: **"you used this function the wrong way."**

When you wrote:

```python
print(my_pleasure.count())
```

Python threw a TypeError because `count()` *requires* an argument, and you gave it none. You essentially called the function incorrectly — and "calling a function incorrectly" is considered a type-related mistake in Python's book.

Think of it this way: `count()` has a specific contract — *"give me one thing to search for, and I'll count it."* By passing nothing, you broke that contract, and Python complained with a TypeError.

So TypeError is really just a general "you're not using this right" error that covers a bunch of situations:

- Wrong number of arguments ← what happened to you
- Mixing incompatible types (like text + number)
- Calling something that isn't callable
- etc.

The error message is what really tells you what went wrong — in your case it said something like `count() takes exactly one argument (0 given)`, which is Python being pretty direct about the actual problem.'''




print(my_pleasure.count('o'))
print(my_pleasure.count('Thank'))
print(my_pleasure.count('k'))

print('-----------------------------')

#Now, let's say I have a big ass string, and I want to find where a certain character is.

print(my_pleasure.find('k')) # This will return '4', meaning k is on the fourth index in the variable called my_pleasure
print(my_pleasure.find('Thank')) # This will return 0, because the world 'Thank' starts on the zero index
print(my_pleasure.find("Fuck")) # This will output -1, which means execution failed because this string does not exist in our variable

print('-----------------------------')
#Now ,let's say I want to replace a part of my string with another. For that, we use the replace.() built-in function, which takes two arguments: The text you will place and the text that will be replaced.

new_my_pleasure = my_pleasure.replace('Thank you, kind sir!', 'Fuck you, Jew!')
print(new_my_pleasure)


print('-----------------------------')
#Now, let's say I have multiple variable that I want to concatenate into one. We use the plus sign operator for that.

conversation = 'Look at this shithole!:'
print(conversation + new_my_pleasure + my_pleasure)