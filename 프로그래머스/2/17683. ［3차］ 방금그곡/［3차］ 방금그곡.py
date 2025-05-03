def solution(m, musicinfos):
    m = ' '.join(m)
    m = m.replace(" #", "#")
    m = m.split(" ")

    def getString(li):
        tmp1 = list(map(int, li[0].split(':')))
        tmp2 = list(map(int, li[1].split(':')))
        minute = 60 * (tmp2[0] - tmp1[0]) + tmp2[1] - tmp1[1]

        txt1 = ' '.join(li[3])
        txt1 = txt1.replace(" #", "#")
        txt1 = txt1.split(" ")
        txt = txt1 * (minute // len(txt1)) + txt1[:minute % len(txt1)]

        for i in range(len(txt) - len(m) + 1):
            if m == txt[i:i + len(m)]:
                return minute
        return 0

    ans1 = "(None)"
    ans2 = 0
    for li in musicinfos:
        tmp = li.split(",")
        minute = getString(tmp)
        if ans2 < minute:
            ans1 = tmp[2]
            ans2 = minute  # ← 이게 빠져서 답이 틀린 거임!
    return ans1
