alfavitEU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' 
b=int(input('Введите шаг сдвига от 0 до 25: '))
if (b>=0) and (b<=25):
        shifrovka=int(input('Вам необходимо: \n 1-Зашифровать текст \n 2-Расшифровать текст '))
        shifr=''
        if shifrovka==1:
          for i in input('Введите сообщение на английском языке, которое надо зашифровать: ').upper():
            pol=alfavitEU.find(i)
            newpol=pol+b 
            if i in alfavitEU:
                shifr+=alfavitEU[newpol]
            else:
                shifr+=i
        elif shifrovka==2:
          for i in input('Введите сообщение, которое надо расшифровать: ').upper():
            pol=alfavitEU.find(i)
            newpol=pol-b 
            if i in alfavitEU:
                shifr+=alfavitEU[newpol]
            else:
                shifr+=i
        print(shifr) 
else:
        print('Ошибка ввода')
        
