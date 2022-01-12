#=============================
#1.Base
#=============================
for x in range(0, 150):
    print(x)

#=============================
#2.Multiples of Five
#=============================

for x in range(5, 1000, 5):
    print(x)

#=============================
#3.Counting, th Dojo Way
#=============================

for x in range(1, 100 + 1):
    if (x%10==0):
        print("Coding Dojo")
    elif (x%5==0):
        print("Coding")
    else:
        print(x)

#=============================
#4.Whoa. That Sucker's huge
#=============================

odd=0

for num in range(0, 500000+1):
    if (num %2 !=0):
        #print(num)
        odd = odd + num
print(odd)

#=============================
#5.Countdown by Fours
#=============================

for x in range(2018, 0, -4):
    print(x)

#=============================
#6.Flexible Counter
#=============================

#Set three variables
lowNum = 2
highNum = 9
mult = 3

for x in range(lowNum,highNum+1):
    if (x==mult):
        print(x)
    elif(x%mult==0):
        print(x)

