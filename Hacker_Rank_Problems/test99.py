from operator import itemgetter

def mixColors(colors, queries):
    res = []
    r = sorted(colors, key=itemgetter(0))
    g = sorted(colors, key=itemgetter(1))
    b = sorted(colors, key=itemgetter(2))
    for query in queries:
        
        res.append("YES")

    return(res)



x =[[1, 3, 5], [5, 3, 1], [1,2,2],[1,1,1],[3,4,4]]

y =[[5, 3, 5], [3, 3, 3]]


print(mixColors(x,y))
