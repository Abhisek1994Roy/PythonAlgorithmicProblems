
def mixColors(colors, queries):
    res = []
    colors = [list(ele) for ele in zip(*colors)]
    for query in queries:
        indices_r=[]
        indices_g=[]
        indices_b=[]
        for i in range(0, len(colors[0])):
            if colors[0][i]==query[0]:
                indices_r.append(i)
            if colors[1][i]==query[1]:
                indices_g.append(i)
            if colors[2][i]==query[2]:
                indices_b.append(i)
        print(indices_r)
        print(indices_g)
        print(indices_b)
        res.append("YES")

    return(res)

x =[[1, 3, 5], [5, 3, 1], [1,2,2],[1,1,1],[3,4,4]]

y =[[5, 3, 5], [3, 3, 3]]


print(mixColors(x,y))
