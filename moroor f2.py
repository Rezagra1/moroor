# mooroor fasl 1 va 2
len()  #shomaresh tedad aza dade sakhtarha 
sorted(object) # object ra bar asas hooroof alefba moratab mikonad
type(a) #  type a ra moshakhas mikonad 
# x = x+1 mosavist ba  x+=1
strings :
    ord(chr) # moadel adadi character ra dar estandard utf-8 ra barmigardanad
    chr(adad)# moadel char adad ra dar estandard utf-8 barmigardanad
    a_str.count('word') # tedad word dakhel a_str ra namayesh midahad
    a_str.count('word',start,stop) # tedad word az start ta stop ra namayesh midahad\
    a_str.replace('a','b')# dar a_str b ra be jaye a migozarad
    a_str.split()
    
lists : 
    a_list[] = #anis migirad va an ra neshan midahad
    a_list[start : stop : step ] 
    a_list.append() # object migirad va hazf mikonad be akhar  
    a_list.extend() # list migirad va ezafe mikonad be akhar 
    a_list.pop()    # andis migirad va an ra hazf mikonad - va barmigardanad
    a_list.remove() # object migirad va avalin mored objet dakhel list ra hazf mikonad 
    a_list.insert(andis, obje) # andis va objet - object ra dar andisash ezafe mikonad 
    a_list.count() # object migirad va an ra mishomard
    a_list.sort() # list ra moratab mikinad , list ra taghir midahad
    a_list.index() # object migirad migooyad chamdomi ast
    a_list.reverse() # list ra sarotah mikonad
    

''.join(a_list) # list , tuple , dic  ra be sring tabdil mikonad 
print("\t",'a') #yek tab a ra jolotar chap mikonad


dictionarys : 
    a_dic[key] # key ra migirad value midahad 
    a_dic[key] += 1 # be value key 1 adad ezafe mikonad 
    a_dic[key] = value # yek kay ba value be dic ezafe mikonad 
    for key, value in a_dic.items() : # keyha va value haye dakhel dic ra barrasi mikonad 
    a_dic.setdefault(key , value) # agar key dakhel dic nabashad ba value be an ezafe mikonad 
    
    
sets: 
    a_set.union(b) # ejtema azaye a_set ba azaye b(har dade sakhtari)
    a_set.differenc(b) # a_set menhaye b ( har dade sakhtari )
    a_set.intersection(b) # azaye moshtarak a_set ba b har dade sakhtari 
    a_set.add('element') # element ra be set ezafe mikonad 
tuples:
    ('a',) # tupel haye tak ozvi hatman kama darand 
    a_tup[start: stop: step]


a , b = b , a # taviz mgadir a va b 
a.split('b') # string a ra 'b' joda mikonad 

formating 
x = 4
y = 6
my_string = 'x = {} and y = {}'.format(x,y) # z,y dakhel format ra betartib dakhel {} ha garar midahad 

    
    
    
