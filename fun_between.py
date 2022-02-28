def combin(n, k):

    d = list(range(0, k))
    yield d

    while True:
        i = k - 1
        while i >= 0 and d[i] + k - i + 1 > n:
            i -= 1
        if i < 0:
            return

        d[i] += 1
        for j in range(i + 1, k):
            d[j] = d[j - 1] + 1

        yield d
        
  def fun_between(v, x0=0, y0=0):
    if v.shape[0] > 1:
        inv = np.arctan2(v[:, 1] - y0, v[:, 0] - x0)
        degree = np.mod(np.degrees(inv), 360)
        print(degree)
        tmp = []
        for c in comb(v.shape[0], 2):
            print(c)
            tmp.append(np.abs(degree[c[0]] - degree[c[1]]))
        print(tmp)
        a = np.array(tmp)
        if a[(a>90) & (a<270)].size > 0:
          return 1
    return 0
    
v = [
    [0, 10],
    [5, 5]
]

v = np.array(v)
a = fun_between(v, x0=0, y0=0)
print(a)
