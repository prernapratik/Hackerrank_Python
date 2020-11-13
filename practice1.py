list_a = [{1: 'a'}, {2: 'b'}, {3: 'c'}]
list_b = [{'a': 'apple'}, {'b': 'ball'}, {'c': 'cat'}]
final = [list_a] + [list_b]
print(final)
for values in zip(list_a,list_b):
    print(values)
    print(f"values[0]{values[0]}::::::values[1]{values[1]}")
    # print(values[0].keys(),values[1].values())
    # for (key,value),(k2,v2) in zip(values[0],values[1]):
    #     print(f"key,value{key,value}:::::k2,v2{k2,v2}")


