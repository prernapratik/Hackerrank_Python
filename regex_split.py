"""Sample Input 0
100,000,000.000

Sample Output 0
100
000
000
000"""

regex_pattern = r"\D"	# Do not delete 'r'.

import re
# print("\n".join(re.split(regex_pattern, input())))

[print(x) for x in re.split('[.,]]',input()) if x]