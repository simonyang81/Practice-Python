from string import Template

s = Template('There are ${howmany} ${lang} Quotation Symbols')

print s.substitute(lang='Python', howmany=3)
print s.safe_substitute()
print s.safe_substitute(lang='Python', howmany=3)
#
# print s.substitute()