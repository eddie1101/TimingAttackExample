def bad_compare(str1, str2):
    if len(str1) != len(str2): return False
    for c1, c2 in zip(str1, str2):
        if c1 != c2: return False
    return True