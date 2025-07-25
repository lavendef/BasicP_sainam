# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
movies_list = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]
a = int(input('แสดงรายชื่อหนังกด 1 : '))
b = int(input('ราคาตั๋วกด 2 : '))
def show_movies(movies_list):
    for mov_name in movies_list:
       
        if a == 1 and b == 2:
            print(mov_name['movie_name'])
            print(mov_name['ticket_price'])
        else:
            print("Error")
show_movies(movies_list)

# # ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
user_age = input('กรอกอายุของท่าน : ')
def check_age(movies_list):
    for aged in movies_list:
        if aged['age_restriction'] == 'G':
            print('Pass! Can watch it now!!')
        elif aged['age_restriction'] != 'G':
            if user_age <= aged['age_restriction']

#     #  ถ้า age_restriction เป็น 'G' ให้ผ่านเลย
#     # ถ้าไม่ใช่ ให้ดึงเลขอายุขั้นต่ำมาเปรียบเทียบกับ user_age

# # ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
# def calculate_price(base_price, genre):
#     # ถ้า genre เป็น 'Horror' บวกเพิ่ม 50 บาท
#     # ถ้าไม่ใช่ คืนราคาเดิม

# # ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
# def buy_ticket(movie_list):
#     #  
#     # 1. เรียก show_movies เพื่อแสดงรายชื่อหนัง
#     # 2. รับค่าตัวเลือกหนังจากผู้ใช้ (1-5)
#     # 3. รับอายุผู้ใช้
#     # 4. ตรวจสอบอายุผ่าน check_age
#     #    - ถ้าไม่ผ่าน ให้แสดงข้อความว่าอายุน้อยเกินไปและ return ออกจากฟังก์ชัน
#     # 5. ให้ผู้ใช้เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack)
#     # 6. คำนวณราคาตั๋วโดยใช้ calculate_price
#     # 7. แสดงผลการซื้อบัตร พร้อมชื่อหนัง, เสียงที่เลือก, ราคาตั๋ว

# def main():
#     #  สร้างรายการหนังเป็น list ของ dict โดยเก็บข้อมูล movie_name, ticket_price, genre, age_restriction
    

#     #  แสดงเมนูให้ผู้ใช้เลือก
#     # 1. แสดงหนังทั้งหมด
#     # 2. ซื้อตั๋วหนัง

#     # รับค่าตัวเลือกเมนูจากผู้ใช้
#     menu = input("เลือกเมนู: ")

#     #  ตรวจสอบเมนูที่เลือก
#     # ถ้าเลือก 1 ให้เรียก show_movies พร้อมส่ง movies
#     # ถ้าเลือก 2 ให้เรียก buy_ticket พร้อมส่ง movies
#     # ถ้าเลือกอื่น ให้แสดงข้อความว่าเมนูไม่ถูกต้อง

# # เรียก main เพื่อเริ่มโปรแกรม
# main()