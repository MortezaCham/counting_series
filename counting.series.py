def counting_series(n):
    digits = 1  # current number of digits
    count = 0   # count of numbers seen so far
    while True:
        # compute the number of digits of numbers with the current number of digits
        numbers_digits = 9 * 10 ** (digits - 1)
        # compute the number of digits of the numbers in the current block
        block_len = numbers_digits * digits
        # if n is within the current block, compute the number at that position
        if n < count + block_len:
            # compute the index within the block
            index = n - count
            # compute the number that contains the digit at that index
            number = 10 ** (digits - 1) + index // digits
            # compute the digit at that index
            eventual_digit = int(str(number)[index % digits])
            return eventual_digit
        # otherwise, skip the current block and move to the next one
        count += block_len
        digits += 1
        
        
        
        
        
        
        

