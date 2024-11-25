def combining_data(data):
  delete = []
  for i in range(len(data)):
    for j in range(i + 1, len(data)):
      if data[i]['lastname'] == data[j]['lastname'] or data[i]['firstname'] == data[j]['firstname'] or data[i]['surname'] == data[j]['surname']:
        for keys in data[i].keys():
            if data[i][keys] == '' and data[j][keys] != '':
              data[i][keys] = data[j][keys]
              delete.append(data[j])
  ob = []
  for i in delete:
    if i not in ob:
      ob.append(i)

  new = []
  for i in range(len(data)):
    if data[i] not in ob:
      new.append(data[i])

  return new