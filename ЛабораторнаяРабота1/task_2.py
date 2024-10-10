# TODO Найдите количество книг, которое можно разместить на дискете

size_of_char = 4
volume = 1.44 * 1024 * 1024

page_count = 100
num_of_strs_on_page = 50
num_of_chars_in_str = 25

count_bytes = num_of_chars_in_str * num_of_strs_on_page * page_count * size_of_char

count_of_books = round(volume // count_bytes)


print("Количество книг, помещающихся на дискету:", count_of_books)
