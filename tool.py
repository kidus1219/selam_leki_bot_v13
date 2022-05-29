def mz_dict_to_query(dictt):
    result = ""
    for x in dictt.items():
        print(x)
        if isinstance(x[1], str):
            result += x[0]+"="+x[1]+"&"
        else:
            for y in x[1]:
                result += x[0] + "=" + y + "&"

    result = result[:-1].replace(" ", "+")
    return result


a = {'title': 'selam leki', 'artist': [0, 'yilma'], 'lyrics': ['eyale', 'eyale', 'eyale', 'eyale']}

#dict_to_query(a)