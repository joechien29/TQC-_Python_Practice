def total_and_mean():
    count = 0
    for i in range(10):
        n = int(input())
        count += n
    return count, count / 10


def main():
    total, mean = total_and_mean()
    print(f'sum = {total}, mean = {mean}')


main()
