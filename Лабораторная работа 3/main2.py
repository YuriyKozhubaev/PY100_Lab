from typing import Union


def delete(list_, index: Union[None, int] = None):
    if index is None:
        return list_[:-1]
    else:
        return list_[:index] + list_[index + 1:]


def delete1(list_, index: Union[None, int] = None): # аккуратно использовать
    if index is None:
        del list_[-1]
        return list_
    del list_[index]
    return list_


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
