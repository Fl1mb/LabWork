# TODO Напишите функцию find_common_participants
def find_common_participants(first_group:str, second_group: str, div:str = ","):
    list1 = first_group.split(div)
    list2 = second_group.split(div)
    result = list(set(list1).intersection(set(list2)))
    result.sort()
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, div="|"))