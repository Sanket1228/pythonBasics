import re

txt = "The rain in spain"

x = re.sub("\s","2",txt)        # Replaces white spaces with digit 2

print(x)