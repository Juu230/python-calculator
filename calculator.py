class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        if(b == 0):
            return "can't divide"
        elif(b < 0):
            while a >= -b:
                a = self.add(a, b)
                result -= 1
            return result
        else:
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return result
    
    def modulo(self, a, b):
        if b == 0:
            return "divisor can't be 0"

        # If the original a was negative, adjust the result to keep it non-negative
        if a < 0 and self.modulo(b,2) != 0 :#(-,odd)
            a = -a
            while a >= b:
                a -= b
            return a + 1
        elif a < 0 and self.modulo(b,2) == 0 :#(-,even)
            a = -a
            while a >= b:
                    a -= b
            return a
        elif b < 0 and self.modulo(b,2) != 0 :#(...,-odd)
            b = -b
            while a >= b:
                a -= b
            return -(a + 1)
        elif b < 0 and self.modulo(b,2) == 0 :#(...,-even)
            b = -b
            while a >= b:
                a -= b
            return -a
        else:
            while a >= b:
                a -= b
            return a



# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(9,-4))
    print("Example: modulo: ", calc.modulo(10, -4))