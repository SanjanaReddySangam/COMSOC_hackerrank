def isvowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']
def score_words(words):
    s=0
    for word in words:
        n=0
        for letter in word:
            if isvowel(letter):
                n+=1
        if(n%2==0):
            s+=2
        else: 
            s+=1
    return s

n = int(input())
words = input().split()
print(score_words(words))
