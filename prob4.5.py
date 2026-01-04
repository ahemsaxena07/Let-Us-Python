s = "The Terribe Tiger Tore The Towel"
pos = s.find('T',0)
print(pos,s[pos])
pos = s.find('T', pos + 1)
print(pos,s[pos])