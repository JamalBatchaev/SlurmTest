def to_snake_case(value: str)->str:
    return value.lower().replace(' ', '_')
    
    #return  '_'.join(value.lower().split()) решение из примера


print(to_snake_case('Some text') ) # some_text
print(to_snake_case('V for Vendetta') ) # v_for_vendetta
print(to_snake_case('Horizon zero dawn') ) # horizon_zero_dawn