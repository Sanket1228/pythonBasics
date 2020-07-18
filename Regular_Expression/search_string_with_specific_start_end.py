import re

txt = "The rain in spain"

x = re.search("^The.*spain$",txt)

if x:
    print("Yes, we find the match")
else:
    print("No match")