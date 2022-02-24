# oop object oriented programming 

the ability that you can creat your own structures with its atributes 
ساختار مند کردن کد برای کار چند نفره روی آن ، بخش بخش کار کردن و غیره 

class example in python : 
    None type , int , list, float , dict , tuple ,str , bool 
    
    
attribute : ویژگی      instance attribute and  class attribute 
method : رفتار        instance method , class method , static method 

instance attribute : ویژگی مختص هر نمونه , such as name or age 
class-attribute : ویژگی مختص خود کلاس , User.attribute 


instance method :  سلف باید داشته باشد ، اما لزوما لازم نیست استفاده شود - رفتار معمول کلاس برای هر نمونه از کلاس
classmethod : رفتار مختص خود کلاس , User.method() , میتوانند متد های دیگر کلاس را فراخوانی کنند 
@classmethod  # use for def a class method 
def add_things(cls, num1, num2):   # User.addthings(3+2)
    return num1 + num 2 


@staticmethod : 
def add_things2(num1 + num2) : """ مانند کلاس متد به خود کلاس اشاره میکنند و نیازی به ساخت آبجکت ندارند 
و نمی توانند اطلاعات کلاس دسترسی داشته باشند  """

    return num1 + num2 
 


for example : 
user1 = User('ali')  # name is an atribute 
user1.Login() # login is an method
User.attribute """its a class attribute  we can not use as user1.attribute 
it directle refers to Class(User) rather than instance of class(user1)"""


self : نمونه ای از کلاس را نشان می دهد 



نکته : ابجمت ها می توانند اتریبیوت های خود را داشته باشند 
p1 = Person ('Ali')
p1.hoby = "sport"

instantiate : calling a class to creat an object mesal # player1 = Classname()
encasulation : ریختن رفتارها یا خصوصیات داخل یک کلاس 
abstraction : hidig of information and giving access to only what necesary 
polymorphism : = Many form 
for example: one method can act differently based on its object 
car.move()  : "drive  car " and  Person.move() "run"


__init__ :  مربوط به تعریف خصوصیت های کلاس هر بار در تعریف  آبجکت جدید فرا خوانی می شود .
__repr__ : تعیین نحوه نمایش آبجکت های کلاس هنگام پرینت گرفتن  
__dict__ : دیکشنری اتریبیوت های کلاس 


decorators (these @property or @classmethod and .... ) apply logic
 or change the behavior of other functions
 
inheritance : وراثت 
class User(person):# کلاس یوزر از کلاس پرسن ارث بری میکند یعنی تمام متد ها و اتریبیوت های آن را دارد
    pass  # new method are overwriten
tamami kelasha az kelas madar object ersbari mikonand


super : 
class person:
    def __init__(self,email):
        self.email= email
class User:
    def __init__(self,name, age , email):
        super().__init__(email) # we no have to use self
        self.name = name
        self.age = age 

MRO # method resolution order 
class A(B,D):
    pass
A.mro()
class A:
    num = 10
    
class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass


introspecion :  درون بینی 
for example we can use dir(list) to see all objects and methods :
    
dunder methods :# we can redefine new act for builtin fanction (+, / , * , del and ...)
# with dunder methods for exmaple (__add__ for + )   :

    
