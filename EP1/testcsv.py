import csv
from datetime import datetime

def writecsv(record_list):
    # newline='' คือให้เรียงต่อกันโดยไม่เว้นช่องว่าง
    # 'a' = append คือการบันทึกค่าไปเรื่อยๆ
    with open('testdata.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(record_list)

dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
record = [dt,'นพดล','B','C']
writecsv(record)
    