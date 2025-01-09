# import sys


# args = sys.argv
    
# num_args = len(args) 

# print(f'Number of argument: {num_args}')
    
    
# module_name = args[0]
# print(f'Module name: {module_name}')
    
    
# numeric_args = [float(arg) for arg in args[1:] if arg.replace('.', '', 1).isdigit()]
# total_sum = sum(numeric_args)
# print(f"Sum of numeric arguments: {total_sum}")
    
    
import sys

print(f"Number of arguments: {len(sys.argv) - 1}")
print(f"Name of the python module: {sys.argv[0]}")
print(f"Sum of all numerical arguments: {sum([int(arg) for arg in sys.argv[1:]])}")