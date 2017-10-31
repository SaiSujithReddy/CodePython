def findCircleNum(A):
    N = len(A)
    print("length of A", N)
    seen = set()
    def dfs(node):
        for nei, adj in enumerate(A[node]):
            print("A[node] is {}".format(A[node]))
            print("nei is {} adj is {}".format(nei,adj))
            if adj and nei not in seen:
                seen.add(nei)
                dfs(nei)
    ans = 0
    for i in xrange(N):
        if i not in seen:
            dfs(i)
            ans += 1

    return ans

A = [[1,1,0],  [1,1,0],  [0,0,1]]
print(findCircleNum(A))

print(enumerate(A))