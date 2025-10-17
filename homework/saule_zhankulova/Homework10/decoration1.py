def finish_me(func):

     def wrapper(*args):
         result = func(*args)
         print('finished')
         return result
     return wrapper


@finish_me
def before_decor(text):
    print(text)


before_decor("print me")
