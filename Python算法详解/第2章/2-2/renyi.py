
# 将列表或者元组 各个元素赋值给变量 ， 最后一个变量可获得多个元素而成为列表
from audioop import avg
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)
record = ('guan', 'guan@toppr.net', '1506907XXXX', '18653154XXX')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)
print(type(phone_numbers))