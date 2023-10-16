
n=0
maxi_secv = 0
maxi = 0
while n !=-1 :
    n = int(input())
    if n !=  0:
        if n > maxi_secv:
            maxi_secv = n
    else:
        print(maxi_secv, " ")
        if maxi_secv > maxi:
            maxi = maxi_secv

print(maxi_secv, " ")
if maxi_secv > maxi:
    maxi = maxi_secv
print(maxi)
