#codigo extraido de: https://www.geeksforgeeks.org/hamming-code-implementation-in-python/#:~:text=Hamming%20code%20is%20a%20set,the%20sender%20to%20the%20receiver.&text=Hamming%20for%20error%20correction
# Python program to dmeonstrate 
# hamming code 

def detectError(arr, nr): 
    n = len(arr) 
    res = 0

    # Calculate parity bits again 
    for i in range(nr): 
        val = 0
        for j in range(1, n + 1): 
            if(j & (2**i) == (2**i)): 
                val = val ^ int(arr[-1 * j]) 

        # Create a binary no by appending 
        # parity bits together. 

        res = res + val*(10**i) 

    # Convert binary to decimal 
    return int(str(res), 2) 
