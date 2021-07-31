
from app import App 
from noise import Noise
from verify import Verify
from transmission import Transmission


# App layer 
app = App()
app.enviar_cadena()

# Verify layer 
ver = Verify()
ver.enviar_cadena_segura(app.msg)

# Noise layer
noi = Noise()
noi.agregar_ruido(ver.bit_msg)

# Transmission layer
tran = Transmission()
tran.enviar_objeto(app.msg, noi.msgnoi)