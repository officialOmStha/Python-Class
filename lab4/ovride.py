#polimorphism , this is over loading.

class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b

        for num in args:
            result *= num
        
        return result
    
c = Calculator()
print(c.multiply())
print(c.multiply(5, 6))
print(c.multiply(5, 6, 7))