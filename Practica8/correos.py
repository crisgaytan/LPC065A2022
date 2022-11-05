import smtplib

correo = input("Ingresa tu correo(exclusivamente outlook):")
contrasena = input("Ingresa tu contraseña:")
destinatario = input("Ingresa tu destinatario:")

message = "este es un mensaje enviado desde python"

server = smtplib.SMTP('smtp.outlook.com', 587)
server.starttls()
server.login(correo, contrasena)

server.sendmail(correo, destinatario, message)

server.quit()

print("correo enviado")
