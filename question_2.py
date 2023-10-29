# Write a programme to count the frequency of words appearing in a string.
# sheena loves eating apple and mango. her sister also loves eating apple and mango.

def freq_word():
    str = input("Enter a string: ")
    lst = str.split()
    dict = {}

    for i in lst:
        if i not in dict.keys():
            dict[i] = 0
        dict[i] = dict[i] + 1
    print(dict)

freq_word()