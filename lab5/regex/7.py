#Program to convert snake case string to camel case string:
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

# Test cases
print(snake_to_camel("this_is_snake_case"))  # thisIsSnakeCase
