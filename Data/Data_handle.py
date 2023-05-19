limits = {}

data = open(file='Data/Pattern.txt',mode='r',encoding='utf-8').read()
data = data.split('\n\n')

if len(data) > 1:
    while data:
        limit, city = data.pop(0).split(' a '), data.pop(0)
        if city not in limits:
            limits[city] = [limit]
        else:
            limits[city].append(limit)
