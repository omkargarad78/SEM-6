def bitwise_operations(string):
    result = []
    for char in string:
        ascii_val = ord(char)
        
        and_result = ascii_val & 127  # AND operation with 127
        result.append(chr(and_result))
        
        xor_result = ascii_val ^ 127  # XOR operation with 127
        result.append(chr(xor_result))
    
    return ''.join(result)

# Original string with proper escape sequence
original_string = "\\Hello World"
processed_string = bitwise_operations(original_string)
print("Processed string: ", processed_string)
