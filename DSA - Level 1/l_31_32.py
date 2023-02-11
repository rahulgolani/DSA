#PYTHAGOREAN TRIPLETS - CHECK IF 3 PROVIDED VALUES CAN FORM A RIGHT ANGLE TRIANGLE OR NOT


def checkPythagoreanTriplet(a,b,c):
    maxNum=max(a,b,c)
    if a==maxNum:
        return a**2==b**2+c**2
    elif b==maxNum:
        return b**2==a**2+c**2
    else:
        return c**2==a**+b**2

if __name__ == '__main__':
    print(checkPythagoreanTriplet(5,13,12))