""" challenge problem taken from
http://www.geeksforgeeks.org/find-kth-character-of-decrypted-string/
Find k’th character of decrypted string
2.5
Given an encoded string where repetitions of substrings are represented as substring followed by count of substrings. For example, if encrypted string is “ab2cd2” and k=4 , so output will be ‘b’ because decrypted string is “ababcdcd” and 4th character is ‘b’.

Note: Frequency of encrypted substring can be of more than one digit. For example, in “ab12c3”, ab is repeated 12 times. No leading 0 is present in frequency of substring.

Examples:

Input: "a2b2c3", k = 5
Output: c
Decrypted string is "aabbccc"

Input : "ab4c2ed3", k = 9
Output : c
Decrypted string is "ababababccededed"
"""
def decrypt_and_substring(string, index):
    # let de_string be variable for decrypt_string
    de_string = ""
    # let portion be the string before integer number multiplier
    portion = ""
    # go through n elements
    for i in string:
        # if it is character, append to portion
        if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
            print "char %s" %i
            portion += i
        # if it a number, repeat portion string number of time in a for loop
        if '0' <= i <= '9':
            for x in range(0, int(i)):
                de_string += portion
            portion = ""
            print de_string
    print de_string[index-1]

decrypt_and_substring("aa2bb3", 5)
decrypt_and_substring("ab4c2ed3", 6)
