T = int(input())
word_list = []
for r in range(T):
    A = input()
    B = input()
    word_list.append(A)
    word_list.append(B)
need_words = []
k = 1
for i in range(int(len(word_list)/2)):
    need_words.append(word_list[k])
    k+=2
use_words = []
z = 0
for i in range(int(len(word_list)/2)):
    use_words.append(word_list[z])
    z+=2
for i in range(len(use_words)):
    word = use_words[i]
    y = need_words[i]
    s = ""
    t = 0  
    for j in word:
        if t < len(y) and j == y[t]:
            s += j
            t += 1
        else:
            s += "#"
    need_words[i] = s
for i in need_words:
    print(i)