str_1= input("enter the first string: ")
str_2= input("enter the second string: ")

if len(str_1)!=len(str_2) :
    print("no, they are not anagram")
else:
    sor_1 = sorted(str_1.lower())
    sor_2 = sorted(str_2.lower())
    if sor_1 == sor_2:
     print("they are anagrams")
    else:
     print("they are not anagram")