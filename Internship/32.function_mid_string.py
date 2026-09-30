def mid_string(s):
    if len(s)%2==0:
        return s

    else:
        mid=len(s)//2
        return s[mid-1]+s[mid]+s[mid+1]

s=input("Enter String:")
print(mid_string(s))