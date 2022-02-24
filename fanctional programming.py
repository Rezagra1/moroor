# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:19:50 2021

@author: Reza
"""
pure fanction :  # شرایط 
    1-خروجی یکسان به ازای ورودی مشابه  در دفعات مختلف اجرا داشته باشد
    2- اثرات جانبی نداشته باشد و اتفاقات داخل خودش بیفتد(مثال چیزی چاپ نکند )
    از دنیای بیرون تاثیر نگیر و تاثیر نگذارد 
# benifits : 
    1- استفاده از این توابع باعث کاهش باگ ، خوانایی ، تست راحت کد و ... میشود
    2- از این تئابع بیش تر استفاده شود 
    3- البته نمشود همه توابع را اینگونه نوشت 
    

map(fun,iterable) - # tabe fun ra migirad va rooye azaye itrable ejra mikonad

filter(fun( returns bool ) , itrable) # az iterable anhaye ke mojaz hastand bagi
# migozarad

zip(iterable1,iterable2, ... ) # az har iterable dakhel toopel garar midahad

reduce(fun , seq , start from)


lambda param:action(param)

#comprehension
list comprehention 
List = [char for char in itrerable ] - ex : [num for num in range(0,100)] or [num for num in range(0,100 if num%2 == 0 )]
or [char.lower() for char in str_list]

dict comprehension 
dic = {key:value for key,velue in iterable if condition}
ex = {k:v*2 for k,v in my_dict.items() if v%2 == 0} or {num:num*2 for num in [1,2,3]}



