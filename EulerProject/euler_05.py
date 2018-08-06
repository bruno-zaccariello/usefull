# Menor multiplo comum dos números entre 1 a 20

def get_result():
    num = 2520
    stop = False
    while not stop:
        print(num)
        stop = True
        for i in range(11,21):
            if num % i != 0:
                num += 2520
                stop = False
    return num