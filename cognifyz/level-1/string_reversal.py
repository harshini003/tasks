#task-1:level 1: String Reversal
def rev(A):
    revers=(A[::-1]) 
    return revers   

for i in range(1,5):
            
            A =input("Enter a string to reversal:") 
            print(rev(A))