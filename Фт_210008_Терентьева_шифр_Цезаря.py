alfavitEU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
b=int(input('������� ��� ������ �� 0 �� 25: '))
shifrovka=int(input('��� ����������: \n 1-����������� ����� \n 2-������������ ����� '))
shifr=''
if shifrovka==1:
        for i in input('������� ��������� �� ���������� �����, ������� ���� �����������: ').upper():
            pol=alfavitEU.find(i)
            newpol=pol+b 
            if i in alfavitEU:
                shifr+=alfavitEU[newpol]
            else:
                shifr+=i
elif shifrovka==2:
        for i in input('������� ���������, ������� ���� ������������: ').upper():
            pol=alfavitEU.find(i)
            newpol=pol-b 
            if i in alfavitEU:
                shifr+=alfavitEU[newpol]
            else:
                shifr+=i
print(shifr)    

