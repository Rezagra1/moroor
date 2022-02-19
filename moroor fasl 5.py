khandan file :
    with open('esme file.ba pasvand ') as f: 
        a = f.read()
        print(a)
"in halat file ra dar masir mojood jostojoo mikonad "

    with open('F:\python projects\dist\esme file.ba pasvand ') as f: 
        a = f.read()
        print(a)
'''dar in halat file dar masire digari ast . dar in soorat masire file ra bayad 
coppy koni'''

    with open('data11.txt') as f :
    for khat in f :
        print(khat)
''' har satr ra jodagane chap mikonad '''
zakhire mohtaviat dakhel list : 
    with open('data11.txt') as f :
        l_khotut = f.readlines()
        print (l_khotut)
        
halat haye baz kardan file : 
    'r' :read - khandan file open('data.txt', 'r') halat pishfarz ham hamin ast 
    'w' :write - neveshtan file open('data.txt', 'w') mohtaviat khod file ra hazf mikonad
    'a' :append - ezafe kardan objecT open('data.txt', 'a') be mohtaviat mojood ezafe mikonad 
    'r+' : read + write : khandan va neveshtan file
    
write :
    with open('data22.txt', "w") as f :
    f.write('chizi ke bayad neveshte shavad/n')
    f.write('harchi2/n')
    f.write('harchi2')
append :
    with open('data22.txt', "a") as f :
    f.write('2525256\n')
    f.write('harchi\n')


try-except-block : 
    try : 
        amali ke doost darim  
    except nameEorre :
        amali ke doost darim 
mesal :
    a = int(input("ye adad benvis :"))
try : 
    print(100/a)
except ZeroDivisionError :
    print('nashod')

halge while True : 
    zamani ke be tekrar bedone shat niaz dashte bashim estefade mikonim 
mesal ba try-except-block : 
print('do adad jahat tagsim avali bar dovomi vared konid ')
print('baraye khorooj "q" ra vared konid ')

while True : 
    a = input('adad aval ra vared konid: ')
    if a == "q":
        break
    b = input('adad aval ra vared konid: ')
    if b == "q":
        break
    try :
        tagsim = float(a)/float(b)
    except ZeroDivisionError:
        print('tagsime adad bar sefr emkan nadarad ')
    else : print(tagsim)
json:
save : import json
with open(esme_file.json, 'w') as f:
    json.dump('chizi ke bayad zakhire shavad', f)
load :
with open(esme_file) as f:
    a = json.load(f)
    print(a)
kar ba excel :
    khandan excel :
import xlrd

esme_file = 'data1.xlsx'

wb = xlrd.open_workbook(esme_file) -- dastrasi be workbook
sh = wb.sheet_by_index(0) -- dastrasi be sheet 
print(sh.cell_value(0,2))  -- dastrasi be selool (satr , sotoon)

    neveshtan excel : 
        import xlwt
wb = xlwt.workbook()
sh1 = wb.add_sheet('sheet1')
sh1.write(0,0,125)
sh1.write(0,1,126)
 
wb.save('data66.xlsx')
