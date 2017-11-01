""" challenge string algorithm taken from
http://www.geeksforgeeks.org/find-kth-character-of-decrypted-string/
Find k’th character of decrypted string
2.5
Given an encoded string where repetitions of substrings are represented as substring followed by count of substrings. For example, if encrypted string is “ab2cd2” and k=4 , so output will be ‘b’ because decrypted string is “ababcdcd” and 4th character is ‘b’.

Note: Frequency of encrypted substring can be of more than one digit. For example, in “ab12c3”, ab is repeated 12 times. No leading 0 is present in frequency of substring.

Examples:

Input: "a2b2c3", k = 5
Output: c
Decrypted string is "aabbccc"

Input : "ab4c12ed3", k = 9
Output : c
Decrypted string is "ababababccccccccccccededed"
"""

def decrypt_and_substring(x_string, index):
    # let decrypted_string be variable for decrypted string
    decrypted_string = ""
    # let str_part be the string before integer number multiplier
    str_part = ""

    # let skip by indicator to skip
    # if already process in case of "00" in 100
    skip_loop = -1

    # go through n elements

    for i, value in enumerate(x_string):
        if skip_loop >= i:
            continue
        # if it is character, append to portion
        if ('a' <= value <= 'z') or ('A' <= value <= 'Z'):
            # print "char %s" % value
            str_part += value
        # if it a number, repeat portion string number of time in a for loop
        if '0' <= value <= '9':
            number_of_substr = value
            # check if next one is integer
            # for example c100 will need to get "00"
            j = i + 1
            while j < len(x_string) and '0' <= x_string[j] <= '9':
                number_of_substr += x_string[j]
                skip_loop = j
                j += 1

            for x in range(0, int(number_of_substr)):
                decrypted_string += str_part
            str_part = ""
    print decrypted_string
    return decrypted_string[index-1]

######### test case 1 ###########
string_position = 5
string_param = "aa2bb3"
print "k-th character at position [%s] for [%s] is [%s]" % \
      (string_position, string_param, decrypt_and_substring(string_param, string_position))
########## test case 2 #########

string_position = 109
string_param = "ab4c100ed3"
print "k-th character at position [%s] for [%s] is [%s]" % \
      (string_position, string_param, decrypt_and_substring(string_param, string_position))


""" program output
aaaabbbbbb
k-th character at position [5] for [aa2bb3] is [b]
ababababccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccededed
k-th character at position [109] for [ab4c100ed3] is [e]
"""
