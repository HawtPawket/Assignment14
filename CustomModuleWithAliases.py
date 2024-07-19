# Task 1: Custom Module with Aliases 

# Problem Statement: Create a custom module named `text_utils.py` with functions for string manipulation 
# (e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions.
# - Expected Outcome: Your main script should be able to use the functions from `text_utils.py` via an alias, demonstrating 
# an understanding of custom module creation and aliasing.




import text_utils as tu

def main():
    normalString = input("What would you like too reverse and capitalize?")

    reversedString = tu.reverse_string(normalString)
    print(reversedString)

    capitalizedString = tu.capitalize_string(normalString)
    print(capitalizedString)
if __name__ == "__main__":
    main()
     
