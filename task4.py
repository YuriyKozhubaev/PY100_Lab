BYTES_ONE_CHAR = 1  # размер одного символа в байтах

# никаких магических чисел
pages = ...  # TODO ввести количество страниц
lines = ...  # TODO ввести количество строк
chars = ...  # TODO ввести количество символов в строке

total_chars = ...  # TODO общее количество символов в книге
total_bytes = ...  # TODO размер одной книги в байтах

disk_size = ...  # TODO размер дискеты в байтах

print(...)  # TODO найти количество книг, которое поместится на дискете

BYTES_ONE_CHAR = 1  # размер одного символа в байтах

# никаких магических чисел
pages = 100
lines = 50
chars = 25

total_chars = pages * lines * chars
total_bytes = total_chars * BYTES_ONE_CHAR

disk_size = 1.44 * 1024 * 1024  # размер в байтах

print(disk_size // total_bytes)

