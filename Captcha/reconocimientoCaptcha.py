try:
        from PIL import Image
except ImportError:
        import Image

import pytesseract
captcha = pytesseract.image_to_string(Image.open('C:\\Users\\lemit\\Documents\\Python Scripts\\Captcha\\captcha1.png'),config='-psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKMNLOPKRSTUVWXYZ')
captcha = captcha.replace(" ", "").strip()
print(captcha)