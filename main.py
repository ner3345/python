#!/usr/bin/python
#lambda 
#gloabel

import re

s = "13417490213"
# s = "12417490213"
r = r"^(13|15|18)\d{8}"

print re.findall(r,s)
