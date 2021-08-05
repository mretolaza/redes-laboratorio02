import random
import hammingClient as hc

class Noise():
  def __init__(self, algoritmo, probabilidad):
    self.noise_msg =""
    self.prob = probabilidad
    self.algoritmo= algoritmo
    self.r = ""
      
  def agregar_ruido(self, msg):
    err = int(len(msg) * 0.01)

    if self.algoritmo == "CRC32":
      print('original', msg)
      crc32 = self.gen_CRC32(msg)
      print('crc32', crc32)

      for x in range(err):
        pos = random.randint(0,99)
        value = str(random.randint(0,1))
        msg = msg[:pos] + str(value) + msg[pos + 1:]

        print('Ruido en:','pos', pos,'value', value)    

      self.noise_msg = msg + crc32
    else:
      #haming

      m = len(msg)
      r = hc.calcRedundantBits(m)
      
      # Determine the positions of Redundant Bits
      arr = hc.posRedundantBits(msg, r)
      
      # Determine the parity bits
      arr = hc.calcParityBits(arr, r)

      for x in range(err):
        pos = random.randint(0,99)
        value = str(random.randint(0,1))
        arr = arr[:pos] + str(value) + arr[pos + 1:]

        print('Ruido en:','pos', pos,'value', value)
      
      self.noise_msg = arr 
      self.r= r

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

  def gen_CRC32(self,ba):
    r = '000'
    dr = ba + r
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