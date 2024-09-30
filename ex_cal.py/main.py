import no as n
import add as d
import sub as s
import mul as m
import div as v
import mod as o
while True:
    print('''
1.add
2.sub
3.mult
4.div
5.mod
6.break
''')
    choice=int(input("enter ur choice:"))
    if choice==1:
        a,b=n.NO()
        d.add(a,b)
    elif choice==2:
        a,b=n.NO()
        s.sub(a,b)
    elif choice==3:
        a,b=n.NO()
        m.mul(a,b)
    elif choice==4:
        a,b=n.NO()
        v.div(a,b)
    elif choice==5:
        a,b=n.NO()
        o.mod(a,b)
    elif choice==6:
        break
    




        
