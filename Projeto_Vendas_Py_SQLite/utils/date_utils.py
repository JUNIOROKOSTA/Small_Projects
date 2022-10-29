from datetime import datetime
from locale import setlocale, LC_ALL

setlocale(LC_ALL, 'pt_BR.utf-8')


def data_now():
    data1 = datetime.now()
    data1 = data1.strftime('%d/%m/%Y')

    return data1

def data_format():
    data1 = datetime.now()
    formatada = data1.strftime('Data Hoje: %d de %B de %Y ( %A ).')
    return formatada



if __name__ == '__main__':
    print(data_now())
    print(data_format())