
saat=int(input('che saati ? '))
daghighe=int(input('che daghighee ? '))
sanie=int(input('che saniee ? '))


def namayesh_zaman () :
    saat2=int(input('chand saat bad ? '))
    daghighe2=int(input('chan daghighe bad ? '))
    sanie2=int(input('chan sanie bad ? '))
    majmo1=saat+saat2
    majmo2=daghighe+daghighe2
    majmo3=sanie+sanie2
    majmo4=('%.2d : %.2d : %.2d'%(majmo1,majmo2,majmo3))

    if majmo1>=12:
        majmo1-=12
    if majmo2>=60:
        majmo2-=60
        majmo1+=1
    if majmo3>=60:
        majmo3-=60
        majmo2+=1
    print('saat shoro %.2d : %.2d : %.2d'%(saat,daghighe,sanie))
    print('saat payan %.2d : %.2d : %.2d'%(majmo1,majmo2,majmo3))
namayesh_zaman()
