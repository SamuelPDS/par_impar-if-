num = int(input("Me diga um numero:"))
num2 = num%2
print(num2)
if num2 == 0:
    print("Esse numero {} é par".format(num))
else:
    print("Esse numero {} é impar".format(num))
