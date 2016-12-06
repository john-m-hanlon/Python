fout = open('johntest.txt', 'w')
line1 = 'This here is the wattle,\n'
fout.write(line1)
line2 = 'the emblem of our land.\n'
fout.write(line2)
x = 52
fout.write(str(x))
camels = 42 
'%d' % camels
line3 = 'I have spotted %d camels.\n' % camels
fout.write(line3)

fout.close()