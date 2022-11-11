
list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


def change_range(list_numbers):
    new_list = list_numbers.copy()
    max_ = new_list[0]  # -math.inf
    max_index = 0
    for index in range(len(new_list)):
        if new_list[index] > max_:
            max_ = new_list[index]
            max_index = index

    new_list[max_index], new_list[-1] = new_list[-1], new_list[max_index]
    print(max_index)
    return new_list