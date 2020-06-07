# nama file p1.py
# Isikan nama anda dan copy semua cell code yang dengan komentar #Graded

# netacad email cth: 'abcd@gmail.com'
email = 'bigmasterindra@yahoo.com'
# name : Indra Nurwibisono

# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

# Graded


def letter_catalog(items, letter='A'):
    pass
    # MULAI KODEMU DI SINI
    l = []
    items = sorted(items)
    for n in range(len(items)):
        if items[n][0].lower() == letter.lower():
            l.append(items[n])
    print(l)

# Graded


def counter_item(items):
    pass
    # MULAI KODEMU DI SINI
    l = {}
    items = sorted(items)
    for n in items:
        if n in l:
            l[n] += 1
        else:
            l[n] = 1
    return l

# Graded


# dua variable berikut jangan diubah
fruits = ['Apple', 'Avocado', 'Banana', 'Blackberries', 'Blueberries',
          'Cherries', 'Date Fruit', 'Grapes', 'Guava', 'Jackfruit', 'Kiwifruit']
prices = [6, 5, 3, 10, 12, 7, 14, 15, 8, 7, 9]

# list buah
chart = ['Blueberries', 'Blueberries', 'Grapes', 'Apple', 'Apple',
         'Apple', 'Blueberries', 'Guava', 'Jackfruit', 'Blueberries', 'Jackfruit']

# MULAI KODEMU DI SINI
fruit_price = dict(zip(fruits, prices))


def total_price(dcounter, fprice):
    pass
    # MULAI KODEMU DI SINI
    totalHarga = {}
    for x in dcounter:
        if x in fprice:
            totalHarga[x] = dcounter[x] * fprice[x]

    return sum(totalHarga.values())

# Graded


def discounted_price(total, discount, minprice=100):
    pass
    # MULAI KODEMU DI SINI
    sum = 0
    if minprice < 100:
        sum = total
    else:
        sum = total - (total * discount / 100)

    return sum

# Graded


def print_summary(items, fprice):
    pass
    # MULAI KODEMU DI SINI
    count = counter_item(items)
    totalHarga = {}
    for x in count:
        if x in fprice:
            totalHarga[x] = count[x] * fprice[x]

    totalHargabuah = total_price(count, fprice)

    for x in count:
        print(count[x], x, ':', totalHarga[x])
    print('total :', totalHargabuah)
    print('discount price :', discounted_price(totalHargabuah, 10, 100))
