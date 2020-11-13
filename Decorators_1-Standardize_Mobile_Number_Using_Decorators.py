"""Sample Input

3
07895462130
919875641230
9195969878
Sample Output

+91 78954 62130
+91 91959 69878
+91 98756 41230"""


def wrapper(f):
    def fun(l):
        if str(l).startswith('0') :
            return f("+91 " +c[-10:-5] + " " + c[-5:] for c in l)
        # complete the function
    return fun


@wrapper
def sort_phone(l):
    print('\n'.join(sorted(l)))


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
