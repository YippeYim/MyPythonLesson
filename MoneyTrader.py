money = int(input("ระบุจำนวนเงินที่ต้องการแลก : "))

Tbaht = money//1000
Fbaht = money%1000//500
Hbaht = money%500//100
left = money%100

print("รับเงินมา______________",money," บาท")
print("แลกได้เป็นแบงค์พัน_______",Tbaht," ฉบับ")
print("แลกได้เป็นแบงค์ห้าร้อย____",Fbaht," ฉบับ")
print("แลกได้เป็นแบงค์ร้อย______",Hbaht," ฉบับ")
print("รวมเป็น_______________",Tbaht+Fbaht+Hbaht," ฉบับ")
if left==0 :
    pass
else :
    print("และเศษอีก ",left," บาท")

print("จบ")
