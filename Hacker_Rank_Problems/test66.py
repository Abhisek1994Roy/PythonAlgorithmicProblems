

def mixColors(colors, queries):
    res = []
    for query in queries:
        rgb=[False, False, False]
        flag = "NO"

        if query in colors:
            flag = "YES"
        else:
            for color in colors:
                if color[0]==query[0] and color[1]<=query[1] and color[2]<=query[2]:
                    rgb[0] = True
                if color[0]<=query[0] and color[1]==query[1] and color[2]<=query[2]:
                    rgb[1] = True
                if color[0]<=query[0] and color[1]<=query[1] and color[2]==query[2]:
                    rgb[2] = True
                if rgb[0] is True and rgb[1] is True and rgb[2] is True:
                    flag = "YES"
                    break
        res.append(flag)
    return(res)








x =[[1, 3, 5], [5, 3, 1]]
y =[[5, 3, 5], [3, 3, 3]]


print(mixColors(x,y))
