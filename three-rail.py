# coding : utf-8
import sys

rail=sys.argv[1]
b_str=sys.argv[2]
a_str=''

if len(b_str)%int(rail)!=0:
    for num in range(len(b_str)//int(rail)):
        a_str+=b_str[num:(len(b_str)%int(rail))*(len(b_str)//int(rail)+1):len(b_str)//int(rail)+1]
        a_str+=b_str[(len(b_str)%int(rail))*(len(b_str)//int(rail)+1)+num::len(b_str)//int(rail)]
    a_str+=b_str[len(b_str)//int(rail):(len(b_str)%int(rail))*(len(b_str)//int(rail)+1):len(b_str)//int(rail)+1]
if len(b_str)%int(rail)==0:
    for num in range(len(b_str)//int(rail)):
        a_str+=b_str[num::int(len(b_str)/int(rail))]
print(a_str)