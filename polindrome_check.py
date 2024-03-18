def is_polindrome(string):
    if string == string[::-1]:
     print(f"The string name {string} is polindrome")
    else:
        print("this string is NOT a polindrome")

string = input("Enter the string: ")
is_polindrome(string)