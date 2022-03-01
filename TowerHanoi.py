towerA,towerB,towerC=[],[],[]
towerAll=[towerA,towerB,towerC]
meaning={"A":towerA,"B":towerB,"C":towerC}

def printtower():
    for n in range(1,len(towerA)+1):
        for l in towerAll:
            print(l[-n]," ",end='')
        print('')
    underline()

def underline():
    for n in range(4):
        print("--",end="")
    print("")

def edittower(size,where,to):
    for n in range(len(meaning[to])):   #เติมsizeที่to
        if (meaning[to])[n]==" ":
            (meaning[to])[n]=size
            break
    for m in range(len(meaning[where])):    #ตัดsizeจากwhere
        if (meaning[where])[m]==size:
            (meaning[where])[m]=" "
            break
    printtower()

#ตัวแปร n , start , aux , dest
def hanoi(n,start,aux,dest):    #(3,"A","B","C")
    if n==0:
        return
    hanoi(n-1,start,dest,aux)
    """
    n=2
        hanoi(1,start,aux,dest)
        ("ย้าย ",2," จาก ",start," ไป ",aux)
            n=1
                ("ย้าย ",1," จาก ",start," ไป ",dest)
    """
    #print("ย้าย ",n," จาก ",start," ไป ",dest)
    edittower(n,start,dest)
    hanoi(n-1,aux,start,dest)

def settower(n):
    for i in range(1,n+1):
        towerA.insert(0,i)
    for j in range(n):
        towerB.append(" ")
        towerC.append(" ")
    hanoi(n,"A","B","C")

num = int(input("insert number : "))
settower(num)
