class Solution:
    def convert(self, s: str, rows: int) -> str:
        if rows==1: return s
        cols = len(s)
        arr={}
        index=0
        i=0
        j=0
        front=True
        while index<cols:
            arr[i,j]=s[index]
            if front:
                if i<rows-1:
                    i=i+1
                elif i == rows-1:
                    i=i-1
                    j=j+1
                    front=False
            else:
                if i>0:
                    i=i-1
                    j=j+1
                elif i == 0:
                    i=i+1
                    front=True
            index+=1
        s_final=""

        for i in range(0,rows):
            for j in range(0,cols):
                if (i,j) in arr:
                    s_final = s_final+arr[i,j]
        return(s_final)


x= Solution()
print(x.convert("PAYPALISHIRING",3))
