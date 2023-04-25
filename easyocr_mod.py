import easyocr
reader = easyocr.Reader(['en'], gpu=False)

result = reader.readtext("test_img.png")
print(result)