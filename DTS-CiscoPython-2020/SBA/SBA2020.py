'''
namafile: sba.py
Lembar kerja/script Latihan SBA
'''
# >>>>>>LEMBAR KERJA>>>>>>>>>
# lembar ini hanya berisi pendefinisian fungsi dan class saja

# email netacad
email = 'bigmasterindra@yahoo.com'

# >>>>>>Soal 1


def fungsiIO(x):
    pass
    # Mulai kode anda dari sini
    nPut = x
    for i in (sorted(nPut)):
        print('*'*i)
# >>>>>>Akhir Soal 1

# >>>>>>Soal 2


def caseShopia(txt):
    pass
    # Mulai kode anda dari sini
    cShp = ''
    for char in txt:
        if char.isalpha() == True:
            if char.islower() == True:
                cShp = cShp + char.upper()
            else:
                cShp = cShp + char.lower()
    return cShp

# >>>>>>Akhir Soal 2


# Jangan diubah biarkan seperti ini
dcur2idr = {'USD': 14425, 'EUR': 16225, 'AUD': 9925, 'CAD': 10500,
            'GBP': 17800, 'CHF': 15200, 'SGD': 10375, 'HKD': 1775,
            'JPY': 132500, 'MYR': 3250, 'SAR': 3500, 'WON': 10750,
            'IDR': 1}

# >>>>>> Soal 3


def usd2eur(usd):
    pass
    # Mulai kode anda dari sini
    usd2idr = usd * dcur2idr['USD']
    idr2eur = usd2idr / dcur2idr['EUR']
    return idr2eur


# >>>>>>Akhir Soal 3


# >>>>>>Soal 4
class MoneyChanger:
    def __init__(self, dcurrency, base='IDR', percent=2):
        pass
        # Mulai kode anda dari sini
        self.base = base
        self.dcurrency = dcurrency
        self.percent = percent
        for i in self.dcurrency:
            if self.dcurrency[i] != self.dcurrency[self.base]:
                self.dcurrency[i] = self.dcurrency[i] / self.dcurrency[self.base]

    def selling_price(self, nominal, curr):
        pass
        # Mulai kode anda dari sini
        c2s = nominal * self.dcurrency[curr]
        sellPercent = (c2s * self.percent) / 100
        sellCurr = c2s + sellPercent
        return sellCurr

    def buying_price(self, nominal, curr):
        pass
        # Mulai kode anda dari sini
        c2b = nominal * self.dcurrency[curr]
        buyPercent = (c2b * self.percent) / 100
        buyCurr = c2b - buyPercent
        return buyCurr

    def change_base(self, new_base):
        pass
        # Mulai kode anda dari sini
        self.base = new_base
        for i in self.dcurrency:
            if self.dcurrency[i] != self.dcurrency[self.base]:
                self.dcurrency[i] = self.dcurrency[i] / self.dcurrency[self.base]

# >>>>>>Akhir Soal 4

# >>>>>>AKHIR LEMBAR KERJA>>>>>>>>>


# KODE DI BAWAH INI UNTUK TESTING
# ANDA BOLEH MEMBUANG SEMUA KODE DI SAAT SUBMISI KE NETACAD

def main():
    pass
    # >>>>>TEST DI SINI>>>>>>
    # gunakan BLOCK MAIN ini untuk mengetes
    # untuk pengetesan kode hanya boleh di bagian sini
    # silakan test sesuka hati di sini

    #############################################
    # uncomment script di bawah ini untuk testing
    #############################################

    print('test soal 1')
    list = (7,4,5,2,1,3)
    fungsiIO(list)  # contoh input: 7 4 5 2 1 3

    print('test soal 2')
    print(caseShopia('thXGth876%^$LMn.'))

    print('test soal 3')
    print(usd2eur(100))  # mengubah 100 USD ke EUR

    print('test soal 4')
    mc = MoneyChanger(dcur2idr, base='SGD', percent=3)  # object mc dengan base EUR
    print('base', mc.base)
    print(mc.selling_price(100, 'USD'))  # nilai jual 100 USD ke EUR (Base)
    print(mc.buying_price(100, 'USD'))  # nilai beli 100 USD ke EUR (Base)
    print(mc.dcurrency)

    mc.change_base('JPY')  # Ganti Base object mc ke IDR
    print('base', mc.base)
    print(mc.selling_price(100, 'GBP'))  # nilai jual 100 USD ke IDR (Base)
    print(mc.buying_price(100, 'GBP'))  # nilai beli 100 USD ke IDR (Base)
    print(mc.dcurrency)

    # >>>>>AKHIR TEST DI SINI>>>>>>


if __name__ == '__main__':
    main()
