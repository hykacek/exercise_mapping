#TASK1
def brute_force(text,p):
    indexes = []
    a = len(text)
    b = len(p)
    for i in range(a-b+1):
        if text[i:i+b] == p:
            indexes.append(i)
    return indexes

def suffix_array(text):
    sorted_list = sorted(range(len(text)), key=lambda i: text[i:])
    return sorted_list

def find_block(text, sa, p):
    a = len(sa)
    b = len(p)
    lo, hi = 0, a
    while lo < hi:
        mid = (lo + hi) // 2
        if text[sa[mid] : sa[mid] + b] < p:
            lo = mid + 1
        else:
            hi = mid
    c = lo

    lo, hi = 0, a
    while lo < hi:
        mid = (lo + hi) // 2
        if text[sa[mid] : sa[mid] + b] <= p:
            lo = mid + 1
        else:
            hi = mid
    d = lo
    return c,d

#TASK2
def bwt(text, sa):
    bwt_str = ""
    for i in sa:
        bwt_str += text[i-1]
    return bwt_str 

def first_occurrence(letters):
    occurrences = {}
    sorted_letters = sorted(letters)
    for idx, char in enumerate(sorted_letters):
        if char not in occurrences:
            occurrences[char] = idx
    return occurrences

def inverse_bwt(bwt):
    first_occ = first_occurrence(bwt)
    k_list = []
    k_dict = {}
    for char in bwt:
        k_dict[char] = k_dict.get(char, 0) + 1
        k_list.append(k_dict[char])

    row = 0
    reverse_bwt_str = ''

    for _ in range(len(bwt) - 1):
        char = bwt[row]
        k = k_list[row]
        reverse_bwt_str += char
        row = first_occ[char] + k - 1

    return "".join(reversed(reverse_bwt_str)) + "$"


