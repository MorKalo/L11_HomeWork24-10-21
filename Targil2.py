targil=input('Please insert an exercise including a result in the structure x + y = z: ')
#targil=targil.replace(" ", "")
list_targil=targil.split()
#print(list_targil)
num1 = float(list_targil[0])
sign=list_targil[1]
num2=float(list_targil[2])
equel=list_targil[3]
result=float(list_targil[4])

if sign=='+':
    print(result==num1+num2)
elif sign=='-':
    print(result == num1 - num2)
elif sign=='/':
    print(result == num1 / num2)
elif sign=='*':
    print(result == num1 * num2)
