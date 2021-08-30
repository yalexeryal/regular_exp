from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="UTF-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
#pprint(contacts_list)

new_dict = {}
for contact in contacts_list:
    contact[0:3] = ' '.join(contact[0:3]).split()
    contact[5] = re.sub(r"(\+7|8)?[\s-]*(\(?(\d{3})\)?)[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})", r"+7(\3)\4-\5-\6",
                        contact[5])
    contact[5] = re.sub(r"\(?доб\.?\s*(\d+)\)?", r"доб.\1", contact[5])

    name = contact[0] + contact[1]

    if name not in new_dict:
        new_dict[name] = contact
    else:
        for i, data in enumerate(contact):
            if data != '':
                new_dict[name][i] = data

new_list = list(new_dict.values())

with open("phonebook.csv", "w", encoding="UTF-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_list)
