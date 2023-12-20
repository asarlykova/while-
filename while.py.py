login=230102002
password=88888888
a=int(input('USERNAME:'))
b=int(input('Password:'))
c=0
while a!=login or b!=password:
    print('Your loggin or password is incorrect, TRY AGAIN!')
    a=int(input('USERNAME:'))
    b=int(input('Password:'))
    c+=1
    if c==3:
        print('Тoo many attempts, please complete identity check')
        break
else:
    print('you are logged in successfully, please wait while it loading')