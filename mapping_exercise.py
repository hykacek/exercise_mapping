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
