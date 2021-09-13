from openpyxl import Workbook
from openpyxl.drawing.image import Image

# pip install pillow 해야함

wb = Workbook()
ws = wb.active

img = Image("img.png")

# C3 위치에 img.png 파일 삽입
ws.add_image(img, "C3")

wb.save("sample_img.xlsx")