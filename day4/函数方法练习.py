def is_f(s):
    s = str(s)
    if s.count('.') == 1:
        left,right = s.split('.')
        if left.isdigit() and right.isdigit():
            return True
        elif left.startswith('-') and left.count('-')==1 \
                and left[1:].isdigit() and right.isdigit():
            return True
    return False



print('is_f',is_f)