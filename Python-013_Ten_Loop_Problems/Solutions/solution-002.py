#QS.02. Sum Of Even Numbers

nth_number = int(input("Enter Your Value:"))

even_sum = 0

if nth_number % 2 != 0:
    print("Please Provide a Even Numbers")
    exit()

for i in range(0, nth_number+1):
    if i % 2 == 0:
        even_sum = even_sum + i

print(even_sum)