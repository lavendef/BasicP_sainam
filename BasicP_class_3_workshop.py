Hp_mon = 1000
Ice_Magic = 66
Tablet = 39
Taobin_soilder = 100
imaginary_friend = 100
face_slap = 5

while True:
    choose = int(input('เลข 1 หรือ 2 ดี :'))

    if choose == 1:
        print('Fight ゜▽゜')
        attack = int(input('ตีกี่รอบดี : '))
        for a in range(attack):
            weapon = input()
            if weapon == 'Ice magic':
                    remain = Hp_mon - Ice_Magic
                    print('เลือดเหลือเท่าไร : ',remain)
                    Hp_mon = remain
            elif weapon == 'Tablet':
                    remain = Hp_mon - Tablet
                    print('เลือดเหลือเท่าไร : ',remain)
                    Hp_mon = remain
            elif weapon == 'Taobin soilder':
                    remain = Hp_mon - Taobin_soilder
                    print('เลือดเหลือเท่าไร : ',remain)
                    Hp_mon = remain
            elif weapon == 'Imaginary_friend':
                    remain = Hp_mon - imaginary_friend
                    print('เลือดเหลือเท่าไร : ',remain)
                    Hp_mon = remain
            elif weapon == 'Face slap':
                    remain = Hp_mon - face_slap
                    print('เลือดเหลือเท่าไร : ',remain)
                    Hp_mon = remain
            else:
                    print('ผิดอันโว้ยยยย')
            if Hp_mon < 0:
                  Hp_mon = 20 
           # comment เรื่องเลือดให้หน่อยพี่ ฮืออ
               

    elif choose == 2:
        print('Bye ╯°□° ╯︵ ┻━┻')
        break
    else:
        print("Error X_X")         
        break
