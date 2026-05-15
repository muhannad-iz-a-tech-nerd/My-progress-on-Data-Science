'''
String indexing is how you access individual characters in a string using their position number (called an index).
In Python, every character in a string has an index starting at 0.
Example:
"Hello"

 H = 0
 e = 1
 l = 2
 l = 3
 o = 4


'''

'''
You can access characters in a string using square brackets [].
Example:
'''
text = "Hello"
print("this is the first index:" + text[0])   # Output: H
print("this is the second index:" + text[1])  # Output: e
print("this is the third index:" + text[2])   # Output: l
print("this is the fourth index:" + text[3])  # Output: l
print("this is the fifth index:" + text[4])   # Output: o

print ('-----------------------------')

'''
#You can also use negative indexing to access characters from the end of the string.
Example:'''
print("this is the last index:" + text[-1])            # Output: o
print("this is the second to last index:" + text[-2])  # Output: l
print("this is the third to last index:" + text[-3])   # Output: l
print("this is the fourth to last index:" + text[-4])  # Output: e
print("this is the fifth to last index:" + text[-5])   # Output: H

print ('-----------------------------')

#Now, let's see what happens if we try to access an index that doesn't exist:
# print(text[5])  # This will raise an IndexError because there is no index

# The code on line 37 is commented out because it raises an IndexError. Here's the error:
r'''
Traceback (most recent call last):
  File "c:\Users\vv3e\Downloads\My progress on Data Science\Python\string_indexing.py", line 37, in <module>
    print(text[5])  # This will raise an IndexError because there is no index
          ~~~~^^^
IndexError: string index out of range
'''

'''
Now, we could also cut from a point in the string to another point in the string, this is called slicing.
Example:
'''
print(text[0:5])  # Output: Hello (from index 0 to index 4, index 5 is not included)
print(text[1:4])  # Output: ell (from index 1 to index 3, index 4 is not included)
print(text[:5])   # Output: Hello (from the beginning of the string to index 4)
print(text[2:5])  # Output: llo (from index 2 to index 4)
