count = 0
def countInversions(array):
    global count
    if len(array) == 0:
        return 0
    
    if len(array) > 1:
    
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]

        countInversions(L)
        countInversions(R)

        i,j,k, = 0,0,0
        # print("here")
        # count = 0
        # print(L,R)
        while i < len(L) and j < len(R):
            # print("L", L[i], "R", R[j])
            if L[i] < R[j]:
                # print("no inversion")
                array[k] = L[i]
                i += 1
            else:
                count += len(L) - i
                # print("inversion with count",count)
                array[k] = R[j]
                j += 1
            k += 1
        #add remaining 
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
        
        return count

if __name__ == "__main__":
    # array = [1, 20, 6, 4, 5]
    NUMLIST_FILENAME = "IntegerArray.txt"
    inFile = open(NUMLIST_FILENAME, 'r')

    with inFile as f:
        array = [int(integers.strip()) for integers in f.readlines()]
        print(countInversions(array))


