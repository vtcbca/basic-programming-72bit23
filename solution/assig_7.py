rows = 3

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("1 ", end="")
        k += 1
   
    k = 0
    print()