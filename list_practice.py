"""Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example
N=4
append 1
append 2
insert 3 1
print
append 1: Append  to the list, arr = [1].
append 2: Append  to the list, arr = [1,2].
insert 3 1: Insert 3 at index 1 , arr = [1,3,2].
print: Print the array.
Output:
[1, 3, 2]

Constraints

The elements added to the list must be integers.
Output Format

Sample input 0::
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample output 0::
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

For each command of type print, print the list on a new line."""


n = input()
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd != "print":
        cmd += "(" + ",".join(args) + ")"
        eval("l."+cmd)
    else:
        print(l)
