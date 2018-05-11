import sys

b_str=sys.argv[1]
a_str=''
if len(b_str)%3!=0:
    for num in range(len(b_str)//3):
        a_str+=b_str[num:(len(b_str)%3)*(len(b_str)//3+1):len(b_str)//3+1]
        a_str+=b_str[(len(b_str)%3)*(len(b_str)//3+1)+num::len(b_str)//3]
    a_str+=b_str[len(b_str)//3:(len(b_str)%3)*(len(b_str)//3+1):len(b_str)//3+1]
if len(b_str)%3==0:
    for num in range(len(b_str)//3):
        a_str+=b_str[num::int(len(b_str)/3)]
print(a_str)