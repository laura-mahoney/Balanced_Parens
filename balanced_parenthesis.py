#given a string, return true or false based on whether the string has balanced parenthesis

"""Does a string have balanced parentheses?

For example::

   >>> has_balanced_parens("()")
   True

   >>> has_balanced_parens("(Oh Noes!)(")
   False

   >>> has_balanced_parens("((There's a bonus open paren here.)")
   False

   >>> has_balanced_parens(")")
   False

   >>> has_balanced_parens("(")
   False

   >>> has_balanced_parens("(This has (too many closes.) ) )")
   False

If you receive a string with no parentheses, consider it balanced::

   >>> has_balanced_parens("Hey...there are no parens here!")
   True
"""


def has_balanced_parens(string):

    left = 0
    right = 0

    for char in string:
        if char == "(":
            left +=1
        if char == ")":
            right += 1

    if left and right <= 0:
        return False

    if left == right:
        return True 
    
    else:
        return False



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n"
