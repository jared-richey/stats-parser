class PrimeNumber:
    def __init__(self,num): 
        self.num = num

    def check_is_prime(self):
        total = 2

        if self.num == 1:
            return("TRUE")
        else:
            for i in range(2,self.num+1):
                if self.num%i != 0:
                    total+=1

            if total == self.num:
                return("TRUE")
            else:
                return("FALSE")
        
    def result(self):
        return(self.num)

max = int(input('Enter a positive integer\n'))

print("Displaying prime numbers and their count in the set [1," + str(max) + "]")

count = 0
for value in range(1,max+1):
   obj = PrimeNumber(value)
   if obj.check_is_prime() == "TRUE":
       count+=1
       print("Prime value: " + str(obj.result()) + " at count #" + str(count))