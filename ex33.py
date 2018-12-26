
numbers = []
k = input(">")

def fun(k):
    i = 0;
    while i<int(k):
     print("At the top i is %d" % i)
     numbers.append(i)
     i = i + 1
     print("Numbers now: ", numbers)
     print("At the bottom i is %d" % i)

fun(k);
print("The numbers: ")
for num in numbers:
    print(num)
