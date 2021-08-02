import random

class Noise():
  def __init__(self):
    self.noise_msg =""
    self.prob = 0.01
      
  def agregar_ruido(self, msg):
    err = int(len(msg) * 0.01)

    print('original', msg)

    for x in range(err):
      pos = random.randint(0,99)
      value = str(random.randint(0,1))
      msg = msg[:pos] + str(value) + msg[pos + 1:]

      print('Ruido en:','pos', pos,'value', value)    

    self.noise_msg = msg 


