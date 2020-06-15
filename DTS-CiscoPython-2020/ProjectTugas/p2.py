# nama file p2.py
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
import random
priority = 2

# netacad email cth: 'abcd@gmail.com'
email = 'bigmasterindra@yahoo.com'

# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini
# Graded


def isPointInCircle(x, y, r, center=(0, 0)):
    # MULAI KODEMU DI SINI
    pass
    dBoolean = None
    if (((x - center[0])**2) + ((y - center[1])**2)) <= r**2:
        return True
    else:
        return False


# Graded


def generateRandomSquarePoints(n, length, center=(0, 0)):
    # MULAI KODEMU DI SINI
    minx = center[0]-length/2
    miny = center[1]-length/2

    # Gunakan list comprehension dengan variable minx, miny, length, dan n
    points = [[random.uniform(minx, minx + length),
               random.uniform(miny, miny + length)] for i in range(n)]

    return points

# Graded


def MCCircleArea(r, n=100, center=(0, 0)):
    # MULAI KODEMU DI SINI
    pass
    titik = 0
    length = r * 2
    points = generateRandomSquarePoints(n, length)

    for i in points:
        if isPointInCircle(i[0], i[1], r) == True:
            titik += 1
    luasLingkaran = (titik / n) * length**2

    return luasLingkaran

# Graded


def LLNPiMC(nsim, nsample):
    # MULAI KODEMU DI SINI
    pass
    totalSim = 0
    for i in range(nsim):
        totalSim += MCCircleArea(1, nsample)
    rataSim = totalSim / nsim

    return rataSim

# Graded


def relativeError(act, est):

    # MULAI KODEMU DI SINI
    pass
    e = abs((est - act) / act) * 100

    return e
