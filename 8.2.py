def is_palindrome(text):
    reversed_text = ''.join(char.lower() for char in text if char.isalnum()) #похоже с 8.
    if reversed_text == reversed_text[::-1]:
     return True
    else:
     return False
assert is_palindrome('A man, a plan, a canal: Panama') == True
assert is_palindrome('0P') == False
assert is_palindrome('a.') == True
assert is_palindrome('aurora') == False
print("OK")