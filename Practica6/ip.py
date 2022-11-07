import socket
import base64

GN = (socket.gethostname())
GHBN = (socket.gethostbyname(socket.gethostname()))


print("Ip publica es:" + (GN))
print("Ip privada es:" + (GHBN))



publi = base64.b64encode(bytes(GN, 'utf-8'))
priv = base64.b64encode(bytes(GHBN, 'utf-8'))

fo = open ("IPS.txt", "w")
fo.write(str(publi))
fo.write(str(priv))

fo.close()
