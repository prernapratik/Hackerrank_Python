"""Input Format

The first line contains a single string denoting s.
The second line contains an integer,k, denoting the length of each subsegment.

Constraints

, where  is the length of
It is guaranteed that  is a multiple of .
Output Format

Print  lines where each line  contains string .

Sample Input

AABCAAADA
3
Sample Output

AB
CA
AD

Explanation
String s is split into 9/3 =3 equal parts of length k=3 . We convert each  to  by removing any subsequent occurrences non-distinct characters in :

We then print each  on a new line."""


def merge_the_tools(string, k):
    # your code goes here
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
