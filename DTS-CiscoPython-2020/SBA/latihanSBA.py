# -*- coding: utf-8 -*-
"""Copy of LatihanSBA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l_tTPzzlCcvzGffC9keb71TLwLRYDx-r
"""

'''
namafile: latihanSBA.py
Lembar kerja/script Latihan SBA
'''
# >>>>>>LEMBAR KERJA>>>>>>>>>
# lembar ini hanya berisi pendefinisian fungsi dan class saja

#email netacad, JANGAN SAMPAI LUPA >>>>>>><<<<<<<
email = 'bigmasterindra@yahoo.com'

#soal 1
class titik2d:  
  pass
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def ambiltitik(self):
    return self.x, self.y
  
  # def tambahkan(self, titik):
  #   tup = self.ambiltitik()
  #   li = list(tup)
  #   li[0] += titik[0]
  #   li[1] += titik[1]
  #   tup = tuple(li)
  #   return tup
  
  def tambahkan(self,titik):
    self.x +=titik.x
    self.y +=titik.y
    
# soal 2
# def run():
#   pass
#   print('Masukkan dua buah nilai untuk titik x dan y dipisahkan dengan spasi')
#   x, y = map(int, input().split())
  # return titik2d(x,y)

def run():
  s = list(map(float, input().split()))
  return titik2d(*s)

# >>>>>>AKHIR LEMBAR KERJA>>>>>>>>>



if __name__ == '__main__':
  # >>>>>TEST DI SINI>>>>>>
  # gunakan BLOCK MAIN ini untuk mengetes

  # untuk pengetesan kode hanya boleh di bagian sini
  # silakan test sesuka hati di sini
  t1 = run()
  print('titik1:',t1.ambiltitik())
  titik3 = (2,3)
  print('titik tambahan:',t1.tambahkan(titik3))

  # >>>>>AKHIR TEST DI SINI>>>>>>