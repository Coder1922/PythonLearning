li=[]
for i in range(1,11):
    li.append(i)
    
first_5=(li[:5])

print("Original list:",li)
print("Extracted first five elements:",first_5)
print("Reversed extracted elements:",first_5[::-1])
