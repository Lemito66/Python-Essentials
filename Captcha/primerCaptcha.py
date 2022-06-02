from captcha.image import ImageCaptcha
import random
import string
caracteresMinusculas = (list(string.ascii_lowercase))
caracteresMayuscula = (list(string.ascii_uppercase))
numeros = (list(string.digits))
charactersComplete = caracteresMinusculas+caracteresMayuscula+numeros
# print(charactersComplete)
image = ImageCaptcha(width=280, height=90)
for i in range(10):
    captcha_char = list()
    for i in range(6):
        letraEscogida = random.choice(charactersComplete)
        captcha_char.append(letraEscogida)
    textoCaptcha = ''.join(captcha_char)
    print(textoCaptcha)
    data = image.generate(textoCaptcha)
    image.write(textoCaptcha, 'C:/Users/lemit/Documents/Python Scripts/Captcha/Imagenes/'+textoCaptcha+'.png')
# print(caracteresMinusculas)
# print(caracteresMayuscula)
""" for i in range(len(caracteresMinusculas)):
    caracteresMinusculas[i]=caracteresMinusculas[i].upper()
print(caracteresMinusculas) """
# print(caracteresMinusculas.upper())
