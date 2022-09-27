def get_bmi(w, h):
    bmi = w / ((h/100) ** 2)
    if bmi < 18.5:
        print('your bmi is under weight')
    elif 18.5 <= bmi < 25:
        print('your bmi is normal')
    elif 25.0 <= bmi < 30:
        print('your bmi is over weihgt')
    elif 30 <= bmi:
        print('your bmi is fat')


def main():
    h = eval(input())
    w = eval(input())
    get_bmi(w, h)


main()
