def solution(files):
    words = []
    nums = {'0','1','2','3','4','5','6','7','8','9'}
    for i in range(len(files)):
        word = files[i]
        idx1 = 0
        idx2 = 0
        for j in range(len(word)):
            if word[j] in nums:
                idx1 = idx2 = j
                for k in range(j, len(word)):
                    if word[k] not in nums:
                        break
                    idx2 = k
                break
        tmp = [word[:idx1], word[idx1:idx2+1]]
        words.append([tmp, word])
        
    words.sort(key = lambda x : int(x[0][1]))
    words.sort(key = lambda x : x[0][0].upper())

    return [itm[1] for itm in words]
    