# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

list_dict = [{"V": "S001"}, {"V": "S002", "f": "asdfa"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
list_uniq = []
for d in list_dict:
    #d = {"V": "S001", "V!": "S00f1"}
    for val in list(d.values()):
        # val = ["S001"; "S00f1"]
        if val not in list_uniq:
            list_uniq.append(val)
print(list_uniq)