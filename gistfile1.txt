H=eval(input("你的身高:"))
W=eval(input("你的體重:"))
BMI=W/(float(H/100))**2
if BMI>=35:
    print("你過度肥胖 BMI=",BMI)
elif BMI>=30:
    print("你中度肥胖 BMI=",BMI)
elif BMI>=27:
    print("你輕度肥胖 BMI=",BMI)
elif BMI>=24:
    print("你過重 BMI=",BMI)
elif BMI>=18.5:
    print("你正常 BMI=",BMI)
else:
    print("你過輕 BMI=",BMI)
