print("                 99乘法表")
print("       ", end=" ")
for i in range (1, 10):
    print("     ", i,end= " ")
    i=i+1
print("================================================================================")
for i in range (1, 10):
    print("  ",i," |",end= " ")
    for j in range (1,10):
        print (format(i*j,'7d'),end= " ")
        j=j+1
    print()
    i=i+1
