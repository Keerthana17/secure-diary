i=0
if c=='w':
 no=raw_input('Enter number of entries to be written : ')
 for i in range(int(no)): 
  dd=raw_input('Please enter day : ')
  mm=raw_input('Please enter month : ')
  yy=raw_input('Please enter year : ')
  hr=raw_input('Please enter hours : ')
  mn=raw_input('Please enter minutes : ')
  fn= 'a'+str(dd)+str(mm)+str(yy)+str(hr)+str(mn)
  ps= 'p'+str(dd)+str(mm)+str(yy)+str(hr)+str(mn)
  print "Password : "
  print ps
  fp=open(fn,"wr")
  dat=raw_input("Enter entry : ")
  fp.write(dat)

i=0
c=raw_input('Enter r to read old entry : ')
if c=='r':
 no=raw_input('Enter number of entries to be read : ')
 for i in range(int(no)):
  dd=raw_input('Please enter day : ')
  mm=raw_input('Please enter month : ')
  yy=raw_input('Please enter year : ')
  hr=raw_input('Please enter hours : ')
  mn=raw_input('Please enter minutes : ')
  fn= 'a'+str(dd)+str(mm)+str(yy)+str(hr)+str(mn)
  ps= 'p'+str(dd)+str(mm)+str(yy)+str(hr)+str(mn)
  ups=raw_input('Enter Password : ')
  if ps!=ups:
   print "Wrong Password.Cannot open file"
  else: 
   print "Correct password. The entry is :"
   fp=open(fn,"r")
   print fp
  


