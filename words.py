n = int(input())
dict = {

}

while n>0:
    word = input()
    if word not in dict:
        dict[word] = 1
        # n-=1
    else:
        dict[word] += 1
    n-=1
print(len(dict))
dictList = list(dict.values())
print(dictList)          