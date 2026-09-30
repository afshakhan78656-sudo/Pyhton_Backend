def palindrome_string(s):
    if s==s[::-1]:
        return True

    else:
        return False

s=input("Enter String:")
if palindrome_string(s):
    print("palindrome string!!")

else:
    print("not palindrome string!!")