def format_fio(data):
    res = []
    for i in data:
        lastname, firstname, surname = (
            i["lastname"].split(" "),
            i["firstname"].split(" "),
            i["surname"].split(" "),
        )
        for j in lastname, firstname, surname:
            res.append(lastname + firstname + surname)
    
    not_repeat = []
    for i in res:
        if i not in not_repeat:
            not_repeat.append(i)
    for i in range(len(not_repeat)):
        r = []
        for j in not_repeat[i]:
            if j != '':
                r.append(j) 
        not_repeat[i] = r

    for i in range(len(data)):
        if len(not_repeat[i]) == 1:
            data[i]["lastname"] = not_repeat[i][0]
        elif len(not_repeat[i]) == 2:
            data[i]["lastname"], data[i]["firstname"] = not_repeat[i][0], not_repeat[i][1]
        elif len(not_repeat[i]) == 3:
            data[i]["lastname"], data[i]["firstname"], data[i]["surname"] = not_repeat[i][0], not_repeat[i][1], not_repeat[i][2]
    
    return data