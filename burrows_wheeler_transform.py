"""
The ending string is $
"""


def bwt(str_to_transform: str) -> str:
    bw_matrix = []
    str_to_transform = '^' + str_to_transform + '|'
    str_len = len(str_to_transform)
    # Create the matrix
    for i in range(0, str_len):
        rotation_str = ''
        for j in range(0, str_len):
            char = str_to_transform[(i + j) % str_len]
            rotation_str += char
        bw_matrix.append(rotation_str)
    bw_matrix = sorted(bw_matrix)
    ret = ''
    for i in range(0, len(bw_matrix)):
        ret += bw_matrix[i][-1:]
    return ret


def reverse_bwt(str_to_revert: str) -> str:
    str_len = len(str_to_revert)
    bw_matrix = [''] * str_len
    for i in range(str_len):
        bw_matrix = sorted(str_to_revert[i] +
                           bw_matrix[i] for i in range(str_len))
    ret = ''
    for row in bw_matrix:
        if row[str_len - 1] == '|':
            ret = ''.join(row)
            break
    ret = ret[1:-1]
    return ret


if __name__ == '__main__':
    s = 'ABSCASDFOASD'
    r = bwt(s)
    print(r)
    s_back = reverse_bwt(r)
    print(s_back)
    print(s == s_back)