#Towers of Hanui solution using backtracking

print("Enter the number of discs")
n=int(input())


def move_disc(height,fromPole, toPole, withPole):
    if height >= 1:
        move_disc(height-1,fromPole,withPole,toPole)
        print("moving disk",height,"from",fromPole,"to",toPole)
        move_disc(height-1,withPole,toPole,fromPole)

move_disc(n,"A","B","C")
