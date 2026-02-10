numbers = [3, 8, 5, 12, 7, 10, 4]

sum_even = 0
sum_odd = 0

for num in numbers:
    if num % 2 == 0:
        print(f"{num} even number")
        sum_even += num
    else:
        print(f"{num} odd number")
        sum_odd += num

print("summery of even numbers:", sum_even)
print("summery of odd numbers:", sum_odd)


