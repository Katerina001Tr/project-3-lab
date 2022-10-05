alfavitEU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'     #Задаю английский алфавит
b=int(input('Введите шаг сдвига от 0 до 25: '))                          #Ввод шага сдвига
if (b>=0) and (b<=25):                                                     #Условие для шага сдвига, чтобы программа выполнялась успешно
        shifrovka=int(input('Вам необходимо: \n 1-Зашифровать текст \n 2-Расшифровать текст '))              #Диалоговый режим с пользователем
        shifr=''
        if shifrovka==1:
          for i in input('Введите сообщение на английском языке, которое надо зашифровать: ').upper():    #Диалоговый режим с пользователем при условии, что мы
            pol=alfavitEU.find(i)                                                                           #шифруем сообщение.
            newpol=pol+b                                             #Происходит поиск букв в заданном алфавите и смещение буквы для шифрования с шагом b.
            if i in alfavitEU:
                shifr+=alfavitEU[newpol]
            else:
                shifr+=i
        elif shifrovka==2:
          for i in input('Введите сообщение, которое надо расшифровать: ').upper():           #Диалоговый режим с пользователем при условии, что мы 
            pol=alfavitEU.find(i)                                                          #расшифровываем сообщение. Ищем буквы в строке и сдвигаем буквы с шагом b.
            newpol=pol-b 
            if i in alfavitEU:
                shifr+=alfavitEU[newpol]
            else:
                shifr+=i
        print(shifr) 
else:
        print('Ошибка ввода')                          #Если значение вышло за диапазон, выводим сообщение об ошибке
        
