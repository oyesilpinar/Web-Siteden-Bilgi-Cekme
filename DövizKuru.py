import requests
from datetime import datetime

url = "https://www.doviz.com/api/v1/currencies/USD/latest"

response = requests.get(url)
jsonverisi = response.json()

dolar = jsonverisi['buying']
last_udate = datetime.fromtimestamp(jsonverisi['update_date'])


def hesapla(dolar, miktar):
    return dolar * miktar


# işlem 1 dolarınızı Tl cinsinden çevirir / işlem 2 doların tl kurunu gösterir
while True:
    islem = input( 'İşlem giriniz' )
    if (islem == '1'):
        tutar = float( input( 'Miktar giriniz' ) )
        print( hesapla( jsonverisi[ 'buying' ], tutar ) )

    elif (islem == '2'):
        print('Dolar :' +str( dolar ) )
        print( 'Son güncellenme : ' + str( last_udate ) )

    else:
        print('Geçersiz işlem')