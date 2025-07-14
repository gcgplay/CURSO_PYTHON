# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')

from datetime import datetime

formato = '%d/%m/%Y'

data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S') #criar
print(data.strftime(formato)) #formatar
print(data.strftime('%d/%m/%Y')) # é uma str

print(data.strftime('%Y'), data.year) # str, int
print(data.strftime('%d'), data.day) # str, int
