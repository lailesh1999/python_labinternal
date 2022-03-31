from datetime import datetime as dt

date_today = dt.now()
register_number = 2117031
PROGRAM_NUMBER = 1
date_today_string = dt.strftime(date_today, '%d-%B-%Y')
result_file_name = f"output_program_{PROGRAM_NUMBER}_{register_number}_{date_today_string}"

print(date_today_string)

file = open(f"{result_file_name}.txt", "w")

str1 = "  AA  BB  CC  DD  EE \n "
str2 = "  BB  CC  FF  GG "

file.writelines(str1)
file.writelines(str2)
file.close()

f1 = open("demo1.txt", 'r')
line1 = f1.readline()
line2 = f1.readline()

line1_list = line1.strip()
line2_list = line2.strip()

line1_list1 = line1_list.split(' ')
line2_list2 = line2_list.split(' ')

line1_reverse = line1_list1[::-1]
line2_reverse = line2_list2[::-1]
print(line1_reverse)
print(line2_reverse)


f1 = open(f"{result_file_name}.txt", "a")
str3 = "\nREVERSE:: \n"
f1.writelines(str3)
f1.writelines(line1_reverse)
f1.writelines("\n")
f1.writelines(line2_reverse)
f1.close()

union_list1 = set(line1_list1).union(set(line2_list2))
f2 = open(f"{result_file_name}.txt", "a")
str4=" \n UNION: \n"
f2.writelines(str4)
f2.writelines(union_list1)
f2.close()


inter_list1 = set(line1_list1).intersection(set(line2_list2))
f3 = open(f"{result_file_name}.txt", "a")
str5=" \n INTERSECTION: \n"
f3.writelines(str5)
f3.writelines(inter_list1)
f3.close()


f1.close()
