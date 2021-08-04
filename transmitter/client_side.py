
from app import App 
from noise import Noise
from verify import Verify
from transmission import Transmission


# App layer 
app = App()

# Verify layer 
ver = Verify()

# Noise layer
noi = Noise()

# Transmission layer
tran = Transmission()

while True:
  app.enviar_cadena()
  ver.enviar_cadena_segura(app.msg)
  noi.agregar_ruido(ver.bit_msg)
  
  #tran.enviar_objeto(app.msg, noi.noise_msg)
  tran.enviar_objeto(noi.r, noi.noise_msg)