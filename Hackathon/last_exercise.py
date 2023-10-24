primo = []

for i in range(1,9999):
    for j in range(2,i):
        if i % j == 0 and i != j:
            primo.append(i)
print(primo)