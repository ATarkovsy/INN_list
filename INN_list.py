
import json
with open('INN_list.json', 'r') as file:
    INN_list = json.load(file)

print(f'Текущий список ИНН {INN_list}')
new_INN = input('Пожалуйста введите необходимый ИНН: \n')
INN_list.append(new_INN)
with open('INN_list.json', 'w') as file:
    json.dump(INN_list, file)
print(f'Обновленный список ИНН {INN_list}')

count = len(INN_list)
print('Текущее количество организаций:' + str(count))

for INN in INN_list:
    print(INN)