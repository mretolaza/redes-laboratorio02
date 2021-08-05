import hammingServer as hs
import bitarray as bitarray
import time

class Verify():
  def __init__(self, algoritmo):
    self.msg_bit = ""
    self.msg_original = ""
    self.algoritmo = algoritmo #"CRC32"
    self.msg_rec = ""
    

  def recibir_cadena_segura(self, msg_bit, msg_original):
    start = time.time()

    self.msg_original = msg_original

    if self.algoritmo == "CRC32":
      #validación del mensaje con CRC32
      res = self.check_CRC32(msg_bit)
      print(res)
      if res == '000':
        print('mensaje verificado!')
      else:
        print('mensaje no verificado, hay ruido')

      #se remueve el crc del mensaje
      self.msg_bit = msg_bit[:-3]
    else: 
      self.msg_bit = msg_bit
      #hamming
      correction = hs.detectError(msg_bit, int(msg_original))
      if correction > 0:
        print("La posición del error es:" + str(correction))
      else: 
        print("Mensaje correcto")
        
    #self.msg_rec = bitarray(bitarray(msg_bit).tolist()).tobytes().decode('utf-8')

    end = time.time()

    print(f"Runtime of the program is {end - start}")

  

  def xor(self, a, b):
    if a == b:
      return '0'
    else:
      return '1'
    

  def operar_xor(self, X, G):
    r =''    
    for x in range(4):
        a = X[x]
        b = G[x]
        temp = self.xor(a, b)
        r = r + str(temp)
    
    if (r[0]) == '0':
        r = r[1:]

    return r

  def check_CRC32(self, ba):
    dr = ba
    g = '1001'
    xg = dr[:4]
    
    res = self.operar_xor(xg,g)    

    for x in range(4,len(dr)):
        xg = res + dr[x]
        #print('xg', xg, xg[0])
        if xg[0] == '1':
            #print(x)
            res = self.operar_xor(xg,g)
            #print('res',res)
        else:
            #print(x)
            temp = xg[1:]
            res = temp
    return res

    
