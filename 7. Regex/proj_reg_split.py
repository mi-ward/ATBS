import re

str_to_split = "dan clancy is the ceo of twitch"
split_param =  ""

str_to_strip = "aaaaaabaaaa"
strip_param = "a"

def reg_split(string, param=r" "):
    if  param:
        pattern = re.compile(r'[^'+ str(param) + r']+')
        mo = pattern.findall(string)
        return mo
    else:
        return reg_split(string)

print(reg_split(str_to_split, split_param))

def reg_strip(string, param=" "):
    if param:
        pattern = re.compile('[^' +param+ '].*[^' +param+ ']|[^' +param+ ']+')
        mo = pattern.search(string)
        if mo is None: 
            return string
        else:
            return mo.group(0)
    else:
        return reg_split(string)
    
print(reg_strip(str_to_strip, strip_param))
print(str_to_strip.strip(strip_param))


print("every dog has it's day".strip() == reg_strip("every dog has it's day"))
print(reg_strip('123a123aaaa123a123','123'))
print(reg_strip('12a3','123'))
print(reg_strip('12a','123'))
print(reg_strip('a3','123'))

