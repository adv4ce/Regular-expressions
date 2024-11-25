from csv import DictReader, DictWriter
import re as r
from format_fio import format_fio
from format_phone import format_phone
from combining_data import combining_data

def main():
  with open("phonebook_raw.csv", "r", newline="", encoding="utf-8") as file:
      f = DictReader(file)
      data = list(f)

  data = format_fio(data)
  data = format_phone(data)
  data = combining_data(data)   
  with open('new_data.csv', 'w', newline='', encoding='utf-8') as file:
     write = DictWriter(file, fieldnames=data[0].keys())
     write.writeheader()
     write.writerows(data)

if __name__ == "__main__":
   main()
