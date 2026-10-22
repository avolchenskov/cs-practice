def count_by_extension(paths):
    d = dict()
    for p in paths:
        r = ''
        if '.' in p and not(p.count('.') == 1 and p[0] == '.'):
      
            r = p.split('.')[-1]
            r = r.lower()
        d[r] = d.get(r, 0) + 1

    return d

def deepest_path(paths):
    res = ''
    for p in paths:
        if p.count('/') > res.count('/'):
            res = p
        elif p.count('/') == res.count('/') and p < res:
            res = p
    return res


def human_size(a: int) -> str:

    if a < 1024:
        return f'{a} Б'
    d = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    
    cnt = 0
    while a >= 1024:
        a /= 1024
        cnt += 1

    return f'{a:.1f} {d[cnt]}'    


