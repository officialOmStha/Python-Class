txt = "Om Shrestha"

f = open("write.txt", "w")
f.write(txt)
f.close()

f = open("write.txt", "a")
f.write(" is a FULLSTACK DEVEOPER")
f.close()