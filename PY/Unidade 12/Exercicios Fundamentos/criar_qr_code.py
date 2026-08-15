# Criando QRCode

import qrcode

# QR Code Simples

imagem = qrcode.make("https://www.instagram.com/olim4gabriel/")
imagem.save("qrcode.png")


# QR Code com imagem

import qrcode
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("https://www.instagram.com/olim4gabriel/")

imagem = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path="../imagens/Exercícios - QR Code - logo.png"

)

# Salva o QR Code gerado
imagem.save("qrcode_logo.png")

print("QR Code gerado com sucesso!")


#QR Code diversos criados ao mesmo tempo

redes_sociais = {
"Facebook": "link",
"Instagram": "link",
"Youtube": "link",
"TikTok": "link"
}

for rede_social, url in redes_sociais.items():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data("https://www.instagram.com/olim4gabriel/")

    imagem = qr.make_image(
        image_factory=StyledPilImage,
        embeded_image_path="../imagens/Exercícios - QR Code - logo.png"

    )

    # Salva o QR Code gerado
    imagem.save("qrcode_logo.png")

    print("QR Code gerado com sucesso!")


    #QR Code diversos criados ao mesmo tempo