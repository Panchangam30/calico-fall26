x = int(input())
word_list = []
for r in range(x):
    
    S = input()
    word_list.append(S)
for s in word_list:
    j = 0
    while j < len(s):
        if s[j] == "O":
            print("[###OREO###]")
            j+=1
        elif s[j:j+2] == "RE":
            print(" [--------] ")
            j+=2
        elif s[j] == "&":
            print()
            j+=1
        else:
            j+=1
