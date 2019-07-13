from math import sqrt
def mysqrt(num,small):
    assert num>0
    assert small>0
    low = 0.0
    high = max(num,1)
    loops=1
    while True and loops<=100:
        a = (high + low) / 2
        test = a ** 2
        if abs(test-num)<small:
            break
        elif test > num:
            high = a
        else:
            low = a
        loops+=1
    return a

if __name__ == '__main__':
    num = input("number:")
    small=0.0000000001
    print(mysqrt(num,small))
    print(sqrt(num))