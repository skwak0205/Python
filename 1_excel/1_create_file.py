'''
실행 : Ctrl + Shift + F10
'''

from openpyxl import Workbook

wb = Workbook()  # 새 워크북(엑셀 파일)을 생성
ws = wb.active  # 현재 활성화된 sheet 가져옴
ws.title = "NadoSheet"  # Worksheet의 이름 변경
wb.save("sample.xlsx")
wb.close()
