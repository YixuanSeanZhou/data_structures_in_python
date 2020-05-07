"""
The ending string is $
"""


def bwt(str_to_transform: str) -> str:
    bw_matrix = []
    str_to_transform += '$'
    str_len = len(str_to_transform)
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
    last_row = list(str_to_revert)
    first_row = sorted(last_row)
    str_len = len(str_to_revert)
    result = [first_row[0]]
    for i in range(1, str_len - 1):
        char_to_search = result[i-1]
        num_occur = result.count(char_to_search)
        count = 0
        for j in range(1, str_len):
            if last_row[j] == char_to_search:
                count += 1
                if num_occur == count:
                    result.append(first_row[j])
                    break

    result.append(last_row[0])
    result.pop(0)
    return ''.join(result)



if __name__ == '__main__':
    print(bwt('THOMASZHOU'))
    print(reverse_bwt('ABB$AILA'))