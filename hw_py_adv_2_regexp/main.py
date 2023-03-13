import re
from pprint import pprint
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

pattern1 = '^(\+7)|^8'
pattern2 = '[\s()-]'
pattern3 = '(доб.)'
for item in contacts_list:
    fio = (item[0]+' '+ item[1]+' '+ item[2])
    item[0] = re.split(r'\s', fio)[0]
    item[1] = re.split(r'\s', fio)[1]
    item[2] = re.split(r'\s', fio)[2]
    phone = item[5]
    ext = None
    phone = re.sub(pattern2,'',re.sub(pattern1,'',phone))
    if re.search(pattern3, phone) != None:
        ext = re.split(pattern3, phone)[2]
        phone = re.split(pattern3, phone)[0]
    phone = re.findall('\d',phone)
    if phone != []:
        code = ''.join(phone[0:3])
        res = f'+7({code}){phone[3]}{phone[4]}{phone[5]}-{phone[6]}{phone[7]}-{phone[8]}{phone[9]}'
        if ext != None:
            res = f'{res} доб.{ext}'
        item[5] = res

i_this = 0
for this in contacts_list:
    i_other = 0
    for other in contacts_list:
        if this[0] == other[0] and this[1] == other[1] and i_this != i_other:
            for i in range(2,7):
                if this[i] == '':
                    this[i] = other[i]
                other[i] = ''
            other[0] = ''
            other[1] = ''
        i_other += 1
    i_this += 1

for i in range(len(contacts_list)-1):
    if contacts_list[i][0] == '' and contacts_list[i][1] == '':
        del contacts_list[i]
                
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  
  datawriter.writerows(contacts_list)