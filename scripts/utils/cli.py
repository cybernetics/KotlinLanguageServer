import sys
import re

alphanum_pattern = re.compile(r"(\d+)|(\D+)") 

def confirm(what):
    result = input(what + " [y/n] ")
    return result.lower().startswith("y")

def alphanum_sort_key(item):
    # Source: https://stackoverflow.com/questions/2669059/how-to-sort-alpha-numeric-set-in-python
    return tuple(int(num) if num else alpha for num, alpha in alphanum_pattern.findall(item))

def require_not_none(description, x):
    if x == None:
        sys.exit(description + " not present")

def prompt_by(what, nodes, describer):
    node_dict = {describer(node): node for node in nodes}
    sorted_described = sorted(node_dict.keys(), key=alphanum_sort_key)
    
    print()
    print(sorted_described)
    print()
    
    last_entry = sorted_described[-1] if len(sorted_described) > 0 else None
    choice = input("Enter a " + what + " to choose [default: " + last_entry + "]: ").strip()
    print()
    
    if len(choice) == 0:
        return node_dict[last_entry]
    elif choice not in node_dict.keys():
        sys.exit("Invalid " + what + "!")
    else:
        return node_dict[choice]
