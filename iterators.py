#-*- coding:utf-8-*-
import itertools
import requests
import pprint

url = 'https://randomuser.me/api/?results=1'
users = requests.get(url).json()

pprint.pprint(users)
# for i in itertools.count(start=20, step=3): iterator with start and step
#     if i > 100: break
#     print(i)
# n = 1
# for i in itertools.cycle("abc"): iterator with cycle (loop)
#     if n > 10: break
#     print(i)
#     n += 1

# letters = list(itertools.repeat("letter:",10))
# print(letters)
# l = list(itertools.combinations("abcd", 2)) # comb items , mixed place (index) 1 param iterator 2 param count
# l1 = list(itertools.combinations_with_replacement('abcd', 2))# comb items with orginal places
# print(l1)

# import time
# pacient = {}
# print("Klinikaga hush kelibsiz !")
# time.sleep(1)
# print('\a')
# print("Iltimos ma'lumotlaringizni kiriting.. ")
# time.sleep(2)
# print('\a')
#
# while 1:
#     name = input('Ismingiz ?\n>>')
#     surname = input('Familyangiz ?\n>>')
#     if name and surname:
#         pacient['fullname'] = "{0} - {1}".format(name,surname)
#     age = int(input('Necha kilosiz ?\n>>'))
#     height = int(input('Boyingiz ?\n>>'))
#     if age and height:
#         pacient['age'] = age
#         pacient['height'] = height
#     disease = input('Kasalliklaringiz \n >>')
    
    
    
        












# count = 0
# ages = 0
# middle = 0
# ls = []
# while True:
#     guess = input('Write your age \n >>>')
#     if guess == 'stop':
#         break
#     guess = int(guess)
#     if guess < 1:
#         print('Write your age again ...')
#     else:
#         count += 1
#     ages += guess
#     middle = ages / count
#     ls.append(guess)
# print(f'Middle age : {math.ceil(middle)}')
# print(f'All ages : {ls}')

# boys = {}
# girls = {}

# while True:
#     name = input('Name :')
#     surname = input('Surname :')
#     middle_ware_dict = {}
#     middle_ware_dict[name] = surname
#     if surname.endswith('va'):
#         girls.update(middle_ware_dict)
#     else:
#         boys.update(middle_ware_dict)
#     print(f'Boys {boys}, Girls {girls}')


# from faker import Faker
# fake = Faker()
# names = []

# for i in range(20):
#     names.append(fake.name())
# count = len(names)
# print(names)
# middle = count // 2
# print(middle)
# right = names[:middle]

# left = names[-middle:]
# print(right)
# left.reverse()
# print(left)
        

        
    
    
    
    
# import cv2
# import numpy as np
# from pyzbar.pyzbar import decode

# def decoder(image):
#     gray_img = cv2.cvtColor(image,0)
#     barcode = decode(gray_img)

#     for obj in barcode:
#         points = obj.polygon
#         (x,y,w,h) = obj.rect
#         pts = np.array(points, np.int32)
#         pts = pts.reshape((-1, 1, 2))
#         cv2.polylines(image, [pts], True, (0, 255, 0), 3)

#         barcodeData = obj.data.decode("utf-8")
#         barcodeType = obj.type
#         string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
        
#         cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
#         print("Barcode: "+barcodeData +" | Type: "+barcodeType)

# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     decoder(frame)
#     cv2.imshow('Image', frame)
#     code = cv2.waitKey(10)
#     if code == ord('q'):
#         break