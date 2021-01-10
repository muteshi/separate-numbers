def separateNumbers(s):
    """
    Returns the start number of the input string if the string has consecutive numbers
    or -1 if not
    """
    # length of the string
    l = len(s)
    
    # initialize variable to hold starting number
    start_str = 0
    
    # Loop through the string until half way
    for i in range(l//2):
        # start finding number
        new_string = s[:i+1]
        #convert to integer
        new_num = int(new_string)

        # save number in start string
        start_str = new_num
        # while loop until when the new string is less than input string
        while len(new_string) < l:
            
            # next number
            new_num += 1
            #concatenate to form new string
            new_string += str(new_num)
            
        # check if new string equals input string
        if s == new_string:
            return start_str
    #string has no consecutive numbers
    return -1
