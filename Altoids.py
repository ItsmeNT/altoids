import requests

print("─█▀▀█ ░█─── ▀▀█▀▀ ░█▀▀▀█ ▀█▀ ░█▀▀▄ ░█▀▀▀█")
print("░█▄▄█ ░█─── ─░█── ░█──░█ ░█─ ░█─░█ ─▀▀▀▄▄")
print("─█─░█ ░█▄▄█ ─░█── ░█▄▄▄█ ▄█▄ ░█▄▄▀ ░█▄▄▄█\n")
print("Chatea a traves de webhooks!")
print("Creado por ReLofi2#7424")
print("Entra al discord del proyecto! https://discord.gg/hxcrW3Z")
print()
link = input("URL Del webhook: ")
print()
nombre = input("Nombre Del webhook: ")
print()
foto = input("Foto de perfil del webhook: ")
print()

while True:
    texto = input(">")

    url = link
    codigojson = {
    "content": texto,
    "username": nombre,
    "avatar_url": foto
    }

    x = requests.post(url, json = codigojson)
