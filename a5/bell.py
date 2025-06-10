# Assignment 5, Task 1
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.2 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
def loveTri(n: int) -> list[list[int]]:
    count = 1
    lst = [[1]]
    while count <= n:
        temp_list = lst[count - 1]
        temp_list_size = len(temp_list)
        last_number_in_list = temp_list[temp_list_size - 1]

        next_row = []
        temp = last_number_in_list
        next_row.append(temp)
        for num in temp_list:
            temp += num
            next_row.append(temp)

        lst.append(next_row)
        count += 1

    return lst
