# Error handling 
"""ارورها همیشه اتفاق می افتند وظیفه ما به عنوان یک برنامه نویس 
این است که این ارور ها را پیش بینی و کنترل کنیم """


    while True : 
        try : 
            age = int(input('Enter your age: '))
            10/age
        except ValueError : # if we receive Value Error this part Execute
            print('Enter a number: ')
            #بهد از اجرای اولین استثنا به خط اول برمیگردیم و استثنای دوم اجرا نمی شود         
        except ZeroDivisionError:  # if we receive Value Error this part Execute
            print('Enter a number greater than 0')
        else: # if try section run successfully 
            print('thank you ')
            break # for Exit while loop 
        finally : # its run anyway even we reach break
            print('I am run every time')
            # its run at the end of every thing 
        print('something ') # its run if no break and contiue execute 
#some triks : 
    
    except (ValueError , ZeroDivisionError):
        pass
        # using one action for two or more Error
    
    except ValueError as err:
        print(f'something went wrong {err}')
        # to define a error description  as a variable 
    except (ValueError , TypeError) as err : 
        print(err)
        
# we can run our own exception and error :
    raise ValueError('just enter a number')
    raise Exception('print something')
    

    
        
