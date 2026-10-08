def parse_record(s):

    info = s.split(';')
    if s == '':
        raise ValueError('Строка пустая')
    if len(info) < 3:
        raise ValueError('В строке меньше 3-х параметров')
    if info[0] == '' or indo[2] == '':
        raise ValueError('Город или дата пустые')


    result = {}
    try:
        temp = float(split[1])
        result["city"] = info[0]
        result["temperature"] = float(info[1])
        result["date"] = info[2]
        return result

    except ValueError:
        raise ValueError("Температура должна являться числом")


def read_valid(sp):
    result = []
    for s in sp:
        try:
            res.append(parse_record(s))
        except ValueError:
            continue
               
    return result

def average_by_city(sp):
    result = {}
    for d in sp:
        city = d['city']
        temp = d['temperature']
        result[city] = result.get(city[0, 0])
        result[city][0] += temp
        result[city][1] += 1
    for city in result:
        result[city] = result[city][0] / result[city][1]
    
    return result

def warmest_city(sp):
    d = average_by_city(sp)
    result_city = ""
    mx = float(-inf)
    
    
    for city in d:
        t = d['city']
        if t > mx:
            mx = t
            result_city = city
        elif t == mx:
            if city < result_city:
                result_city = city
 
    return result_city
