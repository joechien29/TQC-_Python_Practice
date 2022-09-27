def get_gpa(n):
    if 90 <= n <= 100:
        print('your gpa is A')
    elif 80 <= n <= 89:
        print('your gpa is B')
    elif 70 <= n <= 79:
        print('your gpa is C')
    elif 60 <= n <= 69:
        print('your gpa is D')
    elif n <= 59:
        print('your gpa is E')


def main():
    n = int(input())
    get_gpa(n)


main()
