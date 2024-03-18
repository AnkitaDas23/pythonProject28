name_1 = input("what is your name?? ")
name_2 = input("what is your lover name?? ")
combine_name  = name_1+name_2
lower = combine_name.lower()
t = lower.count("t")
r = lower.count("r")
u = lower.count("u")
e = lower.count("e")
true = t+r+u+e

l = lower.count("l")
o = lower.count("o")
v = lower.count("v")
e = lower.count("e")
love = l+o+v+e

love_score = int(str(true)+str(love))

if (love_score<10) or(love_score>90) :
    print(f"your love score is {love_score} and YOU GO TOGETHER LIKE COKE AND MENTOS ")
elif (love_score>=40) and (love_score<=50):
    print(f"your love score is {love_score} and you are perfect together")
else:
    print(f"your love score is {love_score}")