from sorter_api import Sorter
import sys

sort_type = sys.argv[1]
sort_order = sys.argv[2]
filename = sys.argv[3]
output_filename = sys.argv[4]    

SRT = Sorter(sort_type.lower(), sort_order.lower())
file = open(output_filename, "w+")
input = open(filename, "r")
lines = input.readlines()
List = []
for ln in lines[0:len(lines)]:
    if (sort_type == "numbers"):
        numbers=int(ln.strip())
    elif (sort_type == "lexicographically"):
        numbers=str(ln.strip())
    else:
        break
    List.append(numbers)
if (sort_type == "numbers"):
    temp=SRT.sort_nums(List)
elif (sort_type == "lexicographically"):
    temp=SRT.sort_strings(List)
for i in temp:
    file.write(str(i)+"\n")
file.close()