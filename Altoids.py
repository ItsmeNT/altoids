import requests

print ("─█▀▀█ ░█─── ▀▀█▀▀ ░█▀▀▀█ ▀█▀ ░█▀▀▄ ░█▀▀▀█\n░█▄▄█ ░█─── ─░█── ░█──░█ ░█─ ░█─░█ ─▀▀▀▄▄\n░█─░█ ░█▄▄█ ─░█── ░█▄▄▄█ ▄█▄ ░█▄▄▀ ░█▄▄▄█\n\nEnvia mensajes a traves de webhooks de forma comoda\nPerfecto para bromas!\nCreado por ReLofi2#7424\n")

link = input("URL Del webhook: ")
print()
nombre = input("Nombre Del webhook: ")
print()
foto = input("Foto de perfil del webhook: ")
print()
texto = input(">")

url = link
codigojson = {
  "content": texto,
  "username": nombre,
  "avatar_url": foto
}

x = requests.post(url, json = codigojson)

