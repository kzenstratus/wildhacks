new = open('../new_chicago_gang_map.kml', 'w')

with open('../chicago_gang_map.kml', 'r') as f:
  for line in f:
     if 'color' in line:
         new.write("<color>7f1b1c1d</color>\n")
     else:
         new.write(line)

f.close()
new.close()
