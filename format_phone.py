from re import sub

def format_phone(data):
  for i in range(len(data)):
    if len(data[i]['phone']) != 0:
      phone = sub(r'\D', '', data[i]['phone'])[1:]
      if 'доб' in data[i]['phone']:
        dob = sub(' ', '', sub(r'[()]', '', data[i]['phone']))[-4:]
        data[i]['phone'] = f'+7({phone[0:3]})-{phone[3:6]}-{phone[6:8]}-{phone[8:10]} доб.{dob}'
      else:
        data[i]['phone'] = f'+7({phone[0:3]})-{phone[3:6]}-{phone[6:8]}-{phone[8:10]}'
  return data