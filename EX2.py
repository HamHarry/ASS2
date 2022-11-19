print("EX1")
Array1 = [7,5,10,14,3,9,7]
Array2 = [9,10,3,4,2,5,7,1]
print(len(Array1),"And",len(Array2))
print("----------------------------------------------------")

print("EX2")
Array1.insert(7,15)
print(Array1)
print("----------------------------------------------------")

print("EX3")
x = Array1.index(7)
y = Array2.index(7)
print((x),"And",(y))
print("----------------------------------------------------")

print("EX4")
Array1.append(1)
Array2.append(14)
print((Array1),"And",(Array2))
print("----------------------------------------------------")

print("EX5")
Array3 = Array1.copy()
print(Array3)
print("----------------------------------------------------")

print("EX6")
Array3.extend(Array2)
print(Array3)
print("----------------------------------------------------")

print("EX7")
x2 = Array3.count(7)
print(x2)
print("----------------------------------------------------")

print("EX7")
Array3.sort()
print(Array3)
print("----------------------------------------------------")

print("EX7")
Array3.remove(7)
print(Array3)
print("----------------------------------------------------")

print("EX8")
Array4 = Array3.copy()
print(Array4)
print("----------------------------------------------------")

print("EX9")
Array4.reverse()
print(Array4)
print("----------------------------------------------------")

print("EX10")
print(Array3)
print(Array4)
print("----------------------------------------------------")