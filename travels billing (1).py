def detail():
    print ('---RAJ TRAVELS---')
    name=input('customer name:')
    print('place')
    so=input('from:')
    des=input('To:')
    print('car type: 1.mini,2.macro,3.seedan,4.suv')
    car=input('enter the car type:')
    if car in ['mini']:
        print('mini')
        print('4 seater')
        print('1km=rs.8')
    elif car in ['macro']:
        print('macro')
        print('4 seater')
        print('1km=rs.12')
    elif car in ['seedan']:
        print('seedan')
        print('6 seater')
        print('1km=rs.18')
    elif car in ['suv']:
        print('suv')
        print('6-8 seater')
        print('1km=rs.20')
    else:
        print('wrong selection')
    con=int(input('press 1 to confirm or press 0 to change details:'))
    if (con==1):
        print('your details')
        print('customer name:',name)
        print('from:',so)
        print('To:',des)
        print('car type:',car)
    if con == 0:
        detail()
detail()
conr=int(input('press 1 for booking'))
if(conr==1):
    print('your booking is successful')
    print('thank you')
