# coding=gb2312
# ���ϵ���Ϣ���Լ�����Ҫ�Ķ���
def print_matrix(info, m):  # �������
    i = 0;
    j = 0;
    l = len(m)
    print(info)

    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if (j == l):
                print(' |',)
            print('%6.4f' % m[i][j],)
        print
    print


def swap(a, b):
    t = a;
    a = b;
    b = t


def solve(ma, b, n):
    global m;
    m = ma  # ������Ҫ�Ƿ������������ʾ
    global s;

    i = 0;
    j = 0;
    row_pos = 0;
    col_pos = 0;
    ik = 0;
    jk = 0
    mik = 0.0;
    temp = 0.0

    n = len(m)
    # row_pos ���������ѭ��, col_pos ���������ѭ��
    print_matrix("һ��ʼ de ����", m)
    while ((row_pos < n) and (col_pos < n)):
        print("λ�ã�row_pos = %d, col_pos = %d" % (row_pos, col_pos))
        # ѡ��Ԫ
        mik = - 1
        for i in range(row_pos, n):
            if (abs(m[i][col_pos]) > mik):
                mik = abs(m[i][col_pos])
                ik = i

        if (mik == 0.0):
            col_pos = col_pos + 1
            continue

        print_matrix("ѡ��Ԫ", m)

        # ��������
        if (ik != row_pos):
            for j in range(col_pos, n):
                swap(m[row_pos][j], m[ik][j])
                swap(m[row_pos][n], m[ik][n]);  # ����֮�⣿

        print_matrix("��������", m)

        try:
            # ��Ԫ
            m[row_pos][n] /= m[row_pos][col_pos]
        except ZeroDivisionError:
            # �����쳣 һ�����޽�������������³��֡���
            return 0;

        j = n - 1
        while (j >= col_pos):
            m[row_pos][j] /= m[row_pos][col_pos]
            j = j - 1

        for i in range(0, n):
            if (i == row_pos):
                continue
            m[i][n] -= m[row_pos][n] * m[i][col_pos]

            j = n - 1
            while (j >= col_pos):
                m[i][j] -= m[row_pos][j] * m[i][col_pos]
                j = j - 1
        print_matrix("��Ԫ", m)
        row_pos = row_pos + 1;
        col_pos = col_pos + 1
    for i in range(row_pos, n):
        if (abs(m[i][n]) == 0.0):
            return 0
    return 1

if __name__ == '__main__':
    matrix = [[2.0, 0.0, - 2.0, 0.0],
              [0.0, 2.0, - 1.0, 0.0],
              [0.0, 1.0, 0.0, 10.0]]

    i = 0;
    j = 0;
    n = 0
    # ���������
    print_matrix("һ��ʼ�ľ���", matrix)
    # ��ⷽ����, �����������Ŀɽ���Ϣ
    ret = solve(matrix, 0, 0)
    if (ret != 0):
        print("�������н�\n")
    else:
        print("�� ������Ψһ����޽�\n")


    # ��������鼰���
    print_matrix("�����鼰���", matrix)
    for i in range(0, len(m)):
        print("x[%d] = %6.4f" % (i, m[i][len(m)]))



