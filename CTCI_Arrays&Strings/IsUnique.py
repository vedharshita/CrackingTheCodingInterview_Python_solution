#Ques. Implement an algorithm to determine if a string has all unique characters.

#Method 1 Converting to set and checking lengths
##Complexity O(n) to O(n^2) as it is hash set and collision can make complexity higher.
##Iterating over a list is O(n) and adding each element to the hash set is O(1), so the total operation is O(n) minimum.

def IsUnique0(str):
    if(len(str) == len(set(str))):
        return True
    else:
        return False

val = "cracking"
res = IsUnique0(val)
print(res)
val = "coding"
res = IsUnique0(val)
print(res)

#What if you cannot use additional data structures?

#Method 2 Using python str.count() method
##Possible O(n^2) complexity as str.count is in linear time, O(n)

def IsUnique1(str):
    count = 0
    for i in str:
        if str.count(i, 0, len(str)) == 1:
            count +=1
    # print(count)
    if(count == len(str)):
        return True
    else:
        return False

val = "cracking"
res = IsUnique1(val)
print(res)
val = "coding"
res = IsUnique1(val)
print(res)

#Method 3 Using python dict - Counter from collections
##Possible complexity O(n) as it has to iterate over the input, but operations on individual elements remain O(1).

from collections import Counter
def IsUnique2(str):
    for i in Counter(str).values():
        if(i != 1):
            return False
    return True

val = "cracking"
res = IsUnique2(val)
print(res)
val = "coding"
res = IsUnique2(val)
print(res)

#Method 4 Using python dict
##Possible complexity O(n) as it has to iterate over the input, but operations on individual elements remain O(1).

def IsUnique3(str):
    dct = {}
    for i in str:
        dct[i] = dct.get(i,0) + 1
    for i in dct.values():
        if (i != 1):
            return False
    return True


val = "cracking"
res = IsUnique3(val)
print(res)
val = "coding"
res = IsUnique3(val)
print(res)


######################################
# You should first ask your interviewer if the string is an ASCII string or a Unicode string. Asking this question
# will show an eye for detail and a solid foundation in computer science. We'll assume for simplicity the character
# set is ASCII. If this assumption is not valid, we would need to increase the storage size.
#
# We can also immediately return false if the string length exceeds the number of unique characters in the
# alphabet. After all, you can't form a string of 280 unique characters out of a 128-character alphabet.
# I It's also okay to assume 256 characters. This would be the case in extended ASCII. You should
# clarify your assumptions with your interviewer.