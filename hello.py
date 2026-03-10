def square(y):
    print("{} 的平方是 {}".format(y, y**2))

def sum_to_n(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total


x = int(input("請輸入一個整數:"))

if(x <= 0):
    print("您輸入的值是{}，小於等於0".format(x))
else:
    print("您輸入的值是{}，大於0".format(x))
    
    for i in range(1, x+1):
        square(i)

    s = sum_to_n(x)
    print("1+2+...+{} 的總和是 {}".format(x, s))