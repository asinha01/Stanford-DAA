def karatsuba(num1,num2):
   
    # base case - if num1 < 10 and num2<10 -ncannot split further
    if num1<10 or num2<10:
        return num1 * num2
    
    #convert int to str
    snum1, snum2 = str(num1), str(num2)
    m = max(len(snum1), len(snum2)) // 2
   
    #split string into parts
    # split based on mid of longer length
    split1,split2 = len(snum1) - m, len(snum2) - m
   

    a , b = int(snum1[:split1]), int(snum1[split1:])
    c , d = int(snum2[:split2]), int(snum2[split2:])
   
    A = karatsuba(a,c)
    B = karatsuba(b,d)
    C = karatsuba(a+b, c+d)
 
    return A*10**(2*m) + (C-A-B)*10**(m) + B




if __name__ == "__main__":
    print(karatsuba(1234, 5678))











