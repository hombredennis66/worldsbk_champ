#*args= is used to pass a variable number of non-keyword arguments to a function. It allows you to handle more arguments than the number of formal parameters defined in the function. The arguments passed using *args are accessible as a tuple within the function.ug






















#**kwargs = various number of keyword arguments to a function. It allows you to handle more arguments than the number of formal parameters defined in the function. The arguments passed using **kwargs are accessible as a dictionary within the function.

def capital_cities(**kwargs):




    for key, value in kwargs.items():
        print(f"The capital city of {key} is {value}")

        
capital_cities(France="Paris",Spain="Madrid",russia="Moscow",Italy="Rome",Germany="Berlin")
            
              
            
              