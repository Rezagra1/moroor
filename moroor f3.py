sakht functionha : 
    def  name_modual(argiumentha : noevoroody(optional) = 1) ->noekhorooji :
        
    agar mikhhim arg ma megdar difalt deshe bashad ba alamat = mogabel 
    arg an ra moshakhas mikonim
    
    agar bekhahim be andaze delkhah az karbar arg begirim gabl az arg 
    yek * migozarim (*arg) 
    
    baraye dade sakhtarhaye do taei ** migozarim ke dict midahad 
    mesal def my_fun(**karg):
        for k,v in karg.items():
            print(k,v)

    
sakht module ha : 
    pas az zakhire file function ha 
    ye README.txt va
    yek file python ba nam setup.py misazim 
dakhel setup.py :
    from setuptools import setup 
    setup(name :'name modual' , version:'1.01' , py_modual['name file haye pyton nasbi'] )

    sepas cmd ra baz mikonim 
    dakhel masire file python zakhire shode mirim sepas
    py -3 setup.py sdist 
    file feshorde dakhel pushe dist sakhte mishavad .... tamam 

 nasb file gerefte shode ya sakhte shode:
     dar cmd pas az vared shodam be masire file minevisim 
     py -3 -m pip install name file feshorde
     
     nasb tamam mishavad pas az baz kardam python mitavan modul jadid ra import kard 
     
dastoorat cmd :
    D: = raftan be drive d
    cd fasele masire file 
    
barrasi estandard codnevisi ba pycodestyle :
    nasb moduel pycodestyle 
    barrasi file ba raftan be mahale code dakhel cmd ya prompt
    barrasi ba pycodestyle namefile.py
    




        





