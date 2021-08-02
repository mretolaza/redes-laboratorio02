

class Verify():
  def __init__(self):
    self.msg_bit = ""
    self.msg_original = ""
    

  def recibir_cadena_segura(self, msg_bit, msg_original):
    self.msg_original = msg_original

    #validación del mensaje con CRC32
    crc32 = msg_bit[len(msg_bit)-3:]
    res = self.check_CRC32(msg_bit, crc32)

    if res == '000':
      print('mensaje verificado!')
    else:
      print('mensaje no verificado, hay ruido')

    #se remueve el crc del mensaje
    self.msg_bit = msg_bit[:-3]


  def correction():
    #TODO implementar algoritmo de correccion
    pass

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

  def check_CRC32(self, ba, r):
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

    
