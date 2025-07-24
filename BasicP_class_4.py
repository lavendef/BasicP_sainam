# def hello(year):
#     print("Hello World NaJa #" , year)
#     print("Hello World NaJa #" , year)
#     print("Hello World NaJa #" , year)
#     print("Hello World NaJa #" , year)

# hello(31)
# hello("SamSiEh")
# hello(True)
# hello(31.01)

# def summary(a,b):
#     return a+b

# sumthing = summary(10,20)
# print("ผลรวม = ",sumthing)

# def have_rice_spoon(rice,spoon):
#     if rice == True:
#         if spoon == True:
#             return("มีข้าวแล้วนะ เอาช้อนมาแล้วนะ")
          
#         else:
#             return('มีข้าวแล้วนะ แต่เอาส้อมมาทำไม')
#     else:
#         print('อ้าว ข้าวหาย')
#     return 
# print(have_rice_spoon(True,False))

# def calmini(num1,num2,comd):
#     print("กำลังคำนวน : ",num1,comd,num2)
#     if comd == "+":
#         return(num1+num2)
#     elif comd == "-":
#         return(num1-num2)
#     else:
#         return("Are You Dumb (`O´*)")
# print("ผลรวมคือออ : ",calmini(5,5,input()))

#//////////////////////////////////////////////////////////////////////////////////////////////

# listten = ["tripleS","GFriend","Iz*one",24,6,12,True,False]
# print(listten[7])
# listten[7] = "member"
# print(listten)
# print(listten[0])
# print(listten[7])

# listten.append("is")
# print(listten)
# print(listten[0],listten[8],listten[3],listten[7])


# listten.pop(6)
# print(listten)

# for k in listten:
#     print(k,"Kpop")

# boxfruit = ['apple','banana','orange','passion','dragon','stawberry','raspberry','grape','star','mango','pineapple','tamarind']
# def omy():
#     for name in boxfruit:
#         if name == 'apple':
#             print("apple is good")
#         elif name == 'banana':
#             print('banana is good')
#         elif name == 'orange':
#             print('orange is good')
#         else:
#             print("（○□○）??")
    
# omy()

# students = {
#     'name':'Channarongdet Wongyot',
#     'Age':18,
#     'Id':'68130500014',
#     'hobby':'¬_¬'
# }
# check_age = int(students['Age'])
# if check_age >= 18:
#     print('Pass')
# else:
#     print('（○□○）??')

# students = [{
#     'name':'Channarongdet Wongyot',
#     'Age':18,
#     'Id':'68130500014',
#     'hobby':'¬_¬'
# },

# {   'name':'Channi',
#     'Age': 18,
#     'Id':'41000503186',
#     'hobby':'（○□○）??'}]
# for dek in students:
#     print(dek['name'])

students = [{"name": "Thanasorn Dusadeeroj", "age": 19, "ID": 67130500014},
            {"name": "satit", "age": 18, "ID": 6713050047},
            {"name": "channi", "age": 15, "ID": 6713050047}]
for dekD in students:
    if dekD['age'] >= 18:
        print('pass')
    else:
        print('what')



