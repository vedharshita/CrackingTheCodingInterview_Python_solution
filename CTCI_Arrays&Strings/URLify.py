# #Ques. Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string.

#Method 1 direct replace method
##Complexity in worst-case scenario does O(n*m) operations.
#And since it can be up to n/m replacements, in total it should be surprisingly O(n*n)

def URLify0(str):
    str = str.replace(" ","%20")
    print(str)

URLify0("Hello  Boston")

#Method 2
##Complexity O(n).

def URLify1(str):
    lst = []
    for i in range(len(str)-1,0,-1):
        if str[i] == " ":
            lst.append(i)
    print(lst)
    for j in lst:
        str = str[:j] + "%20" + str[j+1:]
    print(str)

URLify1("Hello  Boston")



