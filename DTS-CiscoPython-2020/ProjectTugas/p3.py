# nama file p3.py
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
import math
priority = 1

# netacad email cth: 'abcd@gmail.com'
email = 'bigmasterindra@yahoo.com'

# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini
# Graded


def caesar_encript(txt, shift):
    pass
    # Mulai Kode anda di sini
    cripted = ''
    for char in txt:
        if char.isalpha() == True:
            if char.islower() == True:
                cripted = cripted + chr((ord(char) + shift - 97) % 26 + 97)
            else:
                cripted = cripted + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cripted = cripted + char

    return cripted

# Fungsi Decript caesar


def caesar_decript(chiper, shift):
    return caesar_encript(chiper, -shift)

# Graded

# Fungsi mengacak urutan


def shuffle_order(txt, order):
    return ''.join([txt[i] for i in order])

# Fungsi untuk mengurutkan kembali sesuai order


def deshuffle_order(sftxt, order):
    pass
    # Mulai Kode anda di sini
    n = sorted(order)
    return ''.join(sftxt[order.index(n[i])] for i in n)

# Graded


# convert txt ke dalam bentuk list teks yang lebih pendek
# dan terenkrispi dengan urutan acak setiap batchnya
def send_batch(txt, batch_order, shift=3):
    pass
    # Mulai Kode anda di sini
    cripted = caesar_encript(txt, shift)
    batcher = [cripted[i:i+len(batch_order)]
               for i in range(0, len(cripted), len(batch_order))]
    for i in range(len(batcher)):
        if len(batcher[i]) < 4:
            batcher[i] = batcher[i] + '_'
        batcher[i] = shuffle_order(batcher[i], batch_order)
    return batcher

# batch_cpr: list keluaran send_batch
# fungsi ini akan mengembalikan lagi ke txt semula


def receive_batch(batch_cpr, batch_order, shift=3):
    batch_txt = [caesar_decript(deshuffle_order(
        i, batch_order), shift) for i in batch_cpr]
    return ''.join(batch_txt).strip('_')