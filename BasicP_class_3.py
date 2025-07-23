# rice = False
# spoon = True

# if rice:
#     print("มีข้าวแล้วนะ")
#     if spoon:
#         print('เอาช้อนมาแล้วนะ')
#     else:
#         print('เอาส้อมมาทำไม')
# else:
#     print('อ้าว ข้าวหาย')

#ตื่นก่อน คอยมามอ

# feel_sleepy = True
# shootIgo = True
# if feel_sleepy:
#     print('ตื่นและ')
#     if shootIgo:
#         print('ไปมอกันเถอะ!!')
#     else:
#         print('ไม่ไปและ รถติด')
#     if feel_sleepy == True and shootIgo == True:
#             print("ถึงมอแหละ เย้เย้เย้")
#     else:
#          print('ZZZ ZZZ')
# else:
#     print('ไม่ไปและ ง่วง')

#for - while ahahahahahahahahah

# for u in range(5):
#     print('รอบที่ :',u,'r u ok')
#     if u == 4:
#         for i in range(5):
#             print('Sawatdeekrab :)')
#     else:
#         print('Who are you ??')
# t = True
# for o in range(1,6):
#     print('รอบที่ :',o,'โจทย๋คือไรเอยยย')
#     if o == 3:
#         print('Starter Pack')
#         if t:
#             print('Yes sir')
#         else:
#             print("Nein")
#     else:
#         print("Hello world")

# nummm = int(input('ใส่เลขที่อยากลบได้เลย : '))
# roundd = int(input('ลบกี่รอบดี : '))

# for minus in range(1,roundd):
#     differ = int(input('ลบด้วยไรดี : '))
#     new_numm = nummm-differ
#     print(new_numm)
#     nummm = new_numm
# print('สุดท้ายแล้ว ได้เลข : ',nummm,'ในรอบที่ : ',roundd)


# i = 0
# while i<10:
#     print('sawatdee :)')
#     i = i+1
#     print('รอบที่ :',i)
#     if i == 5:
#         print('let break!!')
#         break

# while True:
#     choose = input('เลข 1 หรือ 2 ดี :')
#     choose = int(choose)
#     if choose == 1:
#         print('please choose agian ¬_¬ ')
#     elif choose == 2:
#         print('เลือกถูกล่ะ ʕ·ᴥ·　ʔ ')
#         break
#     else:
#         print("Error X_X")
#         break

# comment ตรงนี้ให้หน่อยครับ มันผิดตรงไหนครับ ฮือออ
nummm = int(input('ใส่เลขที่อยากลบได้เลย : '))
roundd = int(input('ลบกี่รอบดี : '))
while True:
    differ = int(input('ลบด้วยไรดี : '))
    new_numm = nummm-differ
    print(new_numm)
    nummm = new_numm
    end = 0
    end + 1
    if end >= roundd:
        break
    else:
        continue