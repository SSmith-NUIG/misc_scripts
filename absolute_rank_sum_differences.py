from math import comb
from sympy import binomial


def pexactfrsd_2parts(d,k1,n1,k2,n2):
    result = 0
    i1 = n1*(k1-1)
    for i in range((-i1 -1), (i1+1)):
        result = result + ((part1(i, k1, n1)) * (part2(d-i,k2,n2)))
    return result

def part1(d,k,n):
    yes = 0
    result = 0
    sum2 = 0
    for h in range(0, n+1):
        sum1 = (comb(n,h)) / ((k**h) * ((1-k)**n))
        sum2 = 0
        for i in range(0, h+1):
            for j in range(0, h+1):
                #print(f'K:{k}, i:{i}, j:{j}, d:{d}, h:{h}')
                if ((k*(i-j))-d-h) >= 0:
                    yes = yes + 1
                    print(yes)
                    #print(binomial((k*(i-j)-d+(h-1)), (k*(i-j)-d-h)))
                    sum2 = sum2 + ((-1)**(i-j)) * (comb(h,i)) * (comb(h,j)) * (binomial((k*(i-j)-d+(h-1)), (k*(i-j)-d-h)))
        result = result + (sum1 * sum2)
    return result


def part2(d,k,n):
    yes = 0
    result = 0
    sum2 = 0
    for h in range(0, n+1):
        sum1 = (comb(n,h)) / ((k**h) * ((1-k)**n))
        sum2 = 0
        for i in range(0, h+1):
            for j in range(0, h+1):
                #print(f'K:{k}, i:{i}, j:{j}, d:{d}, h:{h}')
                if ((k*(i-j))-d-h) >= 0:
                    yes = yes + 1
                    print(yes)
                    sum2 = sum2 + ((-1)**(i-j)) * (comb(h,i)) * (comb(h,j)) * (comb((k*(i-j)-d+h), (k*(i-j)-d-h)))
        result = result + (sum1 * sum2)
    return (2 * result)


k=12
n=9
k1=12
n1=9
k2=10
n2=1
d=46
c21 = pexactfrsd_2parts(d, k1, n1, k2, n2)
c21
