#Ques. Given two strings, write a method to decide if one is a permutation of the other.

#Method 1 sorting
##Complexity O(nlogn) as we sorted strings, where n is len of bigger string

def CheckPermutation0(str1,str2):
    str1 = sorted(str1)
    str2 = sorted(str2)
    if str1 == str2:
        return True
    else:
        return False

print(CheckPermutation0("hola","loha"))
print(CheckPermutation0("cracking","coding"))

#Method 2 dict
##Possible complexity O(n) as it has to iterate over the input, but operations on individual elements remain O(1).

def CheckPermutation1(str1,str2):
    dct1 = {}
    dct2 = {}
    for i in str1:
        dct1[i] = dct1.get(i,0) + 1
    for i in str2:
        dct2[i] = dct2.get(i,0) + 1
    if dct1 == dct2:
        # print(dct1,dct2)
        return True
    else:
        return False

print(CheckPermutation1("hola","loha"))
print(CheckPermutation1("cracking","coding"))

#Method 3 Using python dict - Counter from collections
##Possible complexity O(n) as it has to iterate over the input, but operations on individual elements remain O(1).

from collections import Counter
def CheckPermutation2(str1,str2):
    if Counter(str1) == Counter(str2):
        return True
    else:
        return False

print(CheckPermutation2("hola","loha"))
print(CheckPermutation2("cracking","coding"))


######################################################
# if the permutation comparison is case sensitive. That is: is God a permutation of dog? Additionally, we should
# ask if whitespace is significant. We will assume for this problem that the comparison is case sensitive and
# whitespace is significant. So, "god  " is different from "dog". Observe first that strings of different lengths cannot be permutations of each other.
# Note you should always check with your interviewer about the size of the character set.