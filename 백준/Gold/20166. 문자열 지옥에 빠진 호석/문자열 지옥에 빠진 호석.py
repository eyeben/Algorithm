N, M, K = map(int, input().split())
bd = []
for _ in range(N):
    bd.append(list(input()))

words = []
for _ in range(K):
    words.append(input())

dx = [1,0,-1,0, 1,1,-1,-1]
dy = [0,1,0,-1, 1,-1,1,-1]
wordDic = dict()
isNewWord = dict()
def dfs(x, y, idx, word):
    global ans
    if isNewWord[word[:idx]]:
        wordDic[word[:idx]] += 1
    if idx == len(word):
        ans += 1
        return

    for i in range(8):
        nx, ny = (x+dx[i]) % M, (y+dy[i]) % N
        if word[idx] == bd[ny][nx]:

            dfs(nx, ny, idx+1, word)


newWords = sorted(words, key = lambda x: len(x), reverse=True)

for word in newWords:
    ans = 0
    if word in wordDic:
        continue

    for idx in range(1, len(word)+1):
        if word[:idx] in wordDic:
            isNewWord[word[:idx]] = False
        else:
            wordDic[word[:idx]] = 0
            isNewWord[word[:idx]] = True
    for x in range(M):
        for y in range(N):
            if word[0] == bd[y][x]:
                dfs(x,y,1, word)
                wordDic[word] = ans

for word in words:
    print(wordDic[word])