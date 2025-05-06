# Assignment 2, Task 1
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.3 hrs
# Use of AI: Yes
# AI usage details: Wanted to try partial functional approach to string parsing and manipulation in python, doesnt work well

### Your code start here ######
s = input()
t = input()

# step 1
s = s.lower()
t = t.upper()

# step 2
s = ''.join(map(lambda ch: 'm' if ch in 'sla' else ch, s))
'''
temp = ""
for ch in s: 
    if ch == 's' or ch == 'l' or ch == 'a':
        temp += 'm'
    else: 
        temp += ch

s = temp
'''

# step 3
t = ''.join(map(lambda ch: 'T' if ch in 'POIN' else ch, t))
'''
temp = ""
for ch in t: 
    if ch == 'P' or ch == 'O' or ch == 'I' or ch == 'N':
        temp += 'T'
    else: 
        temp += ch

t = temp
'''

# step 4
if s and t:
    temp = s[0]     # fix 
    s = t[0] + s[1:]
    t = temp + t[1:]

# step 5
def replace_last_third_with_mid_third(a, b):
    len_a = len(a)
    len_b = len(b)
    third_a = len_a // 3
    third_b = len_b // 3
    last_a = a[:2 * third_a]
    mid_b = b[third_b:2 * third_b]

    return last_a + mid_b

s = replace_last_third_with_mid_third(s, t)

# step 6
z = s + t

print(z)
