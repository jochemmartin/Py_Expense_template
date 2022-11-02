from PyInquirer import prompt
import csv 
import collections

user_list = []
with open("./users.csv") as f:
    for row in f:
        user_list.append(row.split()[0])

with open('./expense_report.csv', newline='') as f:
    reader = csv.reader(f)
    expense_list = list(reader)

print(expense_list)

def show_status():
    count = {}
    for name in user_list:
        count[name] = float(0)
    for expense in expense_list:
        users = len(expense) - 2
        price = float(expense[0]) / users 
        for i in range (3, len(expense)):
            count[expense[2]] += price
            count[expense[i]] -= price
            # print(expense[i] + " owes " + str(price) + "€ to " + expense[2])
    
    sorted = collections.OrderedDict(count)
    reverse_sorted = collections.OrderedDict(reversed(list(sorted.items())))
    print(reverse_sorted)
    for key,val in reverse_sorted.items():
        if val >= 0:
            print(key + " owes nothing.")
        for k,v in sorted.items():
            if v > 0 and v >= val:
                reverse_sorted[k] -= val
                print(key + " owes " + str(v) + "€ to " + k + ".")
                    

    return