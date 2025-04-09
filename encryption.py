"""d"""
def encryption(word, n, e):
    """_summary_

    Args:
        word (_type_): _description_
        n (_type_): _description_
    """
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 
        'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
        'v', 'w', 'x', 'y', 'z'
        ]
    alphabet2 = [
    'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 
    'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 
    'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я'
    ]

    code = ''
    for i in word:
        s = str(alphabet.index(i)) if i in alphabet else str(alphabet2.index(i))
        if len(s)==1:
            s = '0'+s
        code += s
    block_length = max_block_length(n)
    blocks = [int(code[i:i+block_length]) for i in range(0, len(code), block_length)]
    for i, _ in enumerate(blocks):
        blocks[i] = pow(blocks[i], e, n)

    return code, block_length, blocks

def max_block_length(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    k = 1
    while 10 ** k < n:
        k += 1
    return k
# print(encryption("fcwf", 3551, 17))
# print(encryption("купи", 3551, 17))


def decrypt(code, n, n1, e):
    """_summary_

    Args:
        code (_type_): _description_
        n (_type_): _description_
    """
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 
        'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
        'v', 'w', 'x', 'y', 'z'
        ]
    alphabet2 = [
    'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 
    'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 
    'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я'
    ]
    lst = ''
    result = ''
    d = pow(e, -1, n1)
    for block in code:
        m = (block**d)%n
        lst += str(m).zfill(4)
    print(lst)
    for i in range(0, len(lst), 2):
        result += alphabet[int(lst[i]+lst[i+1])]
    return result
# print(decrypt([144, 1515], 3551, 3432, 17))
# print(decrypt([3153, 2335], 3551, 3432, 17))