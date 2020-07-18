import re

txt = "The rain in spain"

x = re.search('\s',txt)

print("The first white space in text is at position : ",x.start())