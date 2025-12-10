# Find a supplied number is a happy number or not 

def happynumber(n: int) -> bool:

    
    def num_test(num1):
        result = 0
        while num1 >0 :
            reminder = num1 % 10
            result = result + reminder * reminder
            num1 = num1 // 10
        return result 
    
    seen = set()

    while num_test(n) not in seen:
        new_num = num_test(n)
        print('called internal function' , new_num)
        if new_num == 1:
            return True
        else:
            seen.add(new_num)
            n = new_num
    return False

print(happynumber(19))


            



    
