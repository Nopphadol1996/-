
def hello(): # Function แบบไม่มี Parametor
    print('Hello, My name is Nopphadol.')

# hello()

def hellofriend(name): # Function แบบมี Parametor มีกี่ตัวก้ได้
    print(f'Hello, My name is {name}.')

# hellofriend('Nopphadol kanklaew')

def checkNameAge(name, age=80): #Function แบบมี Parametor 2 ตัว และกำหนดค่า default ได้ถ้าหาก user ไม่ใส่จะไม่ Error
    print(f'Hello, My name is {name}.')
    print(f"I'm {age} years old.")

#checkNameAge('Somsak',51)
# checkNameAge(age=70, name='Robert') # ถ้าอยากให้ค่าตรงกันต้องกำหนดอากิวเม้นด้วย
# checkNameAge('Somsri', 100)

def addNumber(x, y): # Function แบบคืนค่าเพื่อนำไปใช้งานต่อ
    return x + y

sum = addNumber(10, 20) # จะต้องสร้างตัวแปรเก็บที่มาจาก function ด้วย
print(sum)


# if else การกำหนดทางเลือกให้กับโปรแกม
# Leap Year
# - หาร 4 ลงตัว หรือ หาร 100 ไม่ลงตัว
# - หาร 400 ลงตัว

'''
year = int(input('ปี ค.ศ. : '))
if year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
    print(f'ค.ศ. {year} เป็น Leap year')
else:
    print(f'ค.ศ. {year} ไม่เป็น Leap year')
'''
color = ['red', 'green', 'blue'] # เก็บข้อมูลตาม index เริ่มจาก 0
# print(color[0])
# print(color[1])
# print(color[2])
# print(color[-1])
color.append('yellow')
# print(color[-1])

for c in color:
    print(c)
