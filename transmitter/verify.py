from bitarray import bitarray

class Verify():
  def __init__(self):
      self.bit_msg = ""
      pass

  def enviar_cadena_segura(self, msg):
    ba = bitarray()
    ba.frombytes(msg.encode('utf-8'))
    self.bit_msg = str(ba)
   
    