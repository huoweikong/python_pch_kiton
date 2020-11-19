records = [
    ('AAA', 1, 2),
    ('BBB', 'hello'),
    ('CCC', 5, 3)
]


def do_foo(x, y):
    print('AAA', x, y)


def do_bar(s):
    print('BBB', s)


for tag, *args in records:  # *无固定个数参数
    if tag == 'AAA':
        do_foo(*args)
    elif tag == 'BBB':
        do_bar(*args)


line = 'guan:ijing234://wef:678d:guan'
uname, *fields, homedir, sh = line.split(':')
print("split:", line.split(':'))
print(uname)
print(*fields)  # *代表无固定合数,自适应
print(homedir)
