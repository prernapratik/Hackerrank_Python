"""Task

You are given a two lists A and B. Your task is to compute their cartesian product A X B.

Example

A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
Note:  and  are sorted lists, and the cartesian product's tuples should be output in sorted order.

Input Format

The first line contains the space separated elements of list .
The second line contains the space separated elements of list .

Both lists have no duplicate integer elements.

Constraints

Output Format

Output the space separated tuples of the cartesian product.

Sample Input

 1 2
 3 4
Sample Output

 (1, 3) (1, 4) (2, 3) (2, 4)"""
from itertools import product


def prod(first, second):
    print(*product(first, second))


if __name__ == "__main__":
    a = [1, 2]
    b = [3, 4]
    prod(a, b)

"""from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))"""