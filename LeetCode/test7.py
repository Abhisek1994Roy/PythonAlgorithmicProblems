class Solution:
    def intToRoman(self, num: int) -> str:
        chars = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}
        k=[1000,500,100,50,10,5,1]
        s=""
        for index,i in enumerate(k):
            print(num, i, s)
            if num>=i:
                if i == 1000 or num <4:
                    count = num//i
                    s=s+count*chars[i]
                    num = num-i*count
                    print("here1")
                    print(s)
                else:
                    l = len(str(num))-1
                    first_digit=int(str(num)[0])
                    if first_digit>=5:
                        print("in")
                        if num>=((10**l)*9):
                            s=s+chars[k[index+1]]+chars[k[index-1]]
                            num = num - ((10**l)*9)
                        else:
                            count = (num-i) // (10**l)
                            print("Count-")
                            print(count)
                            s=s+chars[i]+count*chars[k[index+1]]
                            num=num-i-(count*k[index+1])
                    else:
                        print("out")
                        if num>=((10**l)*4):
                            print("Hereeee")
                            s=s+chars[k[index]]+chars[k[index-1]]
                            num = num - ((10**l)*4)
                        else:
                            print("Out here")
                            count = (num // i)-1
                            print(count)
                            s=s+chars[i]+(count*chars[k[index]])
                            num=num-((count+1)*k[index])
                            print("num")
                            print(num)
        return s



x=Solution()
print(x.intToRoman(41))
