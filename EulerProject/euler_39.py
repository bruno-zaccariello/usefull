# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly
# three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

def pyth(a,b,c):
    return True if (a*a + b*b) == c*c else False

def get_result():
    max = [0, 0]
    for p in range(1001):
        anss = [0, p]
        half = int(p/2)
        print(p)
        for a in range(half):
            for b in range(a, half):
                if a+b > p:
                    break
                for c in range(b, half):
                    if a+b+c > p:
                        break
                    elif a+b+c != p:
                        continue

                    if pyth(a,b,c):
                        anss[0] += 1
        if anss[0] > max[0]:
            max = anss
            print(max)
    return max