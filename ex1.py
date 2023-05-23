def numDivide(num):
    for i in range(num):
        if (num%(i+1)) == 0:
            print(i+1)
        else:
            continue

numDivide(20)

def avgSum():
    temp = 0
    i = 1
    sum = 0
    avg = 0
    while True:
        if i > 1:
            num = int(input(f"please enter number # {i} avg={avg}, sum={sum}: "))
            if num < 0:
                print("Goodbye")
                break
            else:
                sum = temp + num
                avg = sum / i
                temp = sum
                i += 1
        else:
            num = int(input(f"please enter number # {i} : "))
            avg = num
            sum = num
            temp = sum
            i += 1
avgSum()
