# -*- coding: utf-8 -*-


def multiple(x):
    if not x % 3:
        return x
    elif not x % 5:
        return x
    else:
        return 0


def main():
    match_list = [multiple(i) for i in range(1, 1001)]
    return sum(match_list)


if __name__ == '__main__':
    result = main()
    print(result)