چیزهایی که برای رزومه نیاز دارید :
پایتون
جنگو
دیتابیس  : پوسکر اسکوئل
داکر
html , css
دوتا نمونه کار خوب
داکر مزیت خوبی است باعث میشود از بقیه جلوتر باشید






start
after activate venv:

django-admin startproject filename .
good to use congif for filename : django-admin startproject congif .

to see project :
python manage.py runserver

make new app :
python manage.py startapp appname
شناساندن اپ به برنامه :
config > setting > installed app > add appname

شناساندن اینترپرتر به برنامه  :
file > setting > project name > python interpreter > add > select

ارتباط با دیتابیس:
python manage.py makemigrations appname
python manage.py migrate

python manage.py createsuperuser

autheticaion : # احراز هویت
هنکام ساختن  لاگین تنها وظیفه ما ساخت یو ار ال و وصل کردن آن به اپ جنگو آوث جنگو میباشد
ویو  یو آر ال  ها توسط جنگو از پیش طراحی شده است
سپس ساخت تمپلیت در آدرس زیر :
regisiration/login.html

>config>urls> path('accounts/', include(django.contrib.auth.urls)) : وصل کردن اپ آوث چنگو به یو آر ال

برای ساخت  صفحه  ثبت نام کاربر باید یو آر ال ویو و تمپلیت را خودمان بسازیم
> بعد از لاگین جنگو برای همه تمپلیت ها یک متغییر یوزر ارسال میکند
user.is_authenticated == Ture


django.contrib.auth
setting > end of the line :
LOGIN_REDIRECT_URL = "name of url" # ریدایرکت شدن به این صفحه در صورت  لوگ این شدن
LOGOUT_REDIRECT_URL = "name of url" # ریدایرکت شدن به این صفحه در صورت لاگ آوت شدن

gitignore :
*.sqlite3
.idea/
venv/
__pycache__/


deploye :
install heroku cli
type in commend line :
pip install gunicorn
>
pip freeze > requirements.txt
>
in the project folder > make a file > Procfile :
open in txt mode > write this on file >  web: gunicorn config.wsgi --log-file - > save

in setting file > find ALLOWED_HOSTS > ADD '*'
push project to git

heroku login > heroku create > heroku config:set DISABLE_COLLECTSTATIC=1 >
git push heroku main  > heroku run python mange.py migrate

you can run python code in heroku  with  : heroku run ....

> heroku open  #make site online


CustomUser :
به دلیل این که بعد از مایگریت اول نمیتوان مدل یوز اصلی جنگو را تغییر داد
همیشه باید در ابتدای پروژه از کاستوم یوزر استفاده کرد تا بتوانیم بعدا  در مدل یوزر تغییرات ایجاد کنیم

> ابتدا داخل اپ جدید که برای مدیریت اکانتا میسازم کلاس کاستوم یوزر را تغریف میکنیم
>setting > akhar khat > AUTH_USER_MODEL = "Accounts.CustomUser"
>null : baraye database , blanck : baraye validation
null : برای کاراکتر متنی از این استفاده نمیکنیم فقط بلنک را ترو میگذاریم
>سپس فرم مربوط به ساخت یوزر و فرم مربوط به ویرایش یوزر را میسازیم
سپس فرم های ساخته شده را  داخل ادمین تعریف میکنیم
>model create > form create > admin edith

Crispy_forms :

>pip install django-crispy-forms
>add 'crispy_forms', to installed app in setting
> CRISPY_TEMPLATE_PACK = 'bootstrap4' in setiings

>use {% load crispy_forms_tags %} after extend tag  in template
> then  user form|crispy

password forgot and change # email config
for send mail active :
> setiings > EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


دانستن اسامی و اصطلاحات مهم است
Idioms :
{{ }} # interpreting data
{% %} #template tags
 | #template filter

#validate user uploded images :
>pip install pillow
