def a(S):
    i, j = 0, len(S) - 1
    S = list(S)
    while i < j:
        while not S[i].isalpha():
            i += 1
            if i >= len(S) - 1:
                return ''.join(S)
        while not S[j].isalpha():
            j -= 1
            if j <= 0:
                return ''.join(S)
        if i >= j:
            return ''.join(S)
        if S[i].isalnum() and S[j].isalpha():
            s = S[i]
            S[i] = S[j]
            S[j] = s
            i += 1
            j -= 1
    return ''.join(S)
    # if not S or S.__len__()<=2:
    #     return S
    # l = []
    # for i in S:
    #     if not i.isalpha():
    #         l.append(i)
    #     else:
    #         l.append('\\')
    # i = 0
    # while l[i] == '\\' and i<len(S)-1:
    #     i +=1
    # for j in range(len(S)-1,-1):
    #     if S[j].isalpha():
    #         l[i] = S[j]
    #         i+=1
    # return ''.join(l)


print(a("tNH95P=TV"))
