def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_

def get_count_char(str_):
    dict_ = {}
    str_ = str_.lower() # без него но в for
    for char in str_: # str_.lower()
        if char.isalpha():
            if char in dict_.keys():
                dict_[char] += 1
            else:
                dict_[char] = 1
    return dict_
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
