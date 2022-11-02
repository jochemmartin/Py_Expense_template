from PyInquirer import prompt
import csv 

user_list = []
with open("./users.csv") as f:
    for row in f:
        user_list.append(row.split()[0])

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": user_list
    },
    
]

def ask_other_users(spender):
    other_users_question = [
        {
            "type":"checkbox",
            "name":"other_spender",
            'qmark': '😃',
            "message":"Other users involved: ",
            "choices": [{"name" : name} for name in user_list if name != spender]
        }
    ]
    return prompt(other_users_question)

def new_expense(*args):
    infos = prompt(expense_questions)
    infos_other = ask_other_users(infos["spender"])
    print(infos_other)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    f = open('./expense_report.csv', 'a', newline='')
    writer = csv.writer(f)
    row = list(infos.values()) + infos_other["other_spender"]
    writer.writerow(row)
    f.close()
    return True


