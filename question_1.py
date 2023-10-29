# Write a python programme to find out common letters b/w two strings. 
# 1) NAINA       2) REENE


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
s1 = set(str1)
s2 = set(str2)
lst = s1 & s2
print(lst)
