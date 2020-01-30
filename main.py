def tail_rev(in_string,rev_string):
    if in_string=='':
        return rev_string
    else:
        rev_string+=in_string[-1]
        return tail_rev(in_string[:-1],rev_string)

in_string=input("Enter String: ")
rev_string=tail_rev(in_string,'')
print(f"Reverse is {rev_string}") 

#Code gained from @AshishIsh on Stack Overflow