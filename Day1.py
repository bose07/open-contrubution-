#open file
fo=open("E:\\Day1.txt",'a')                                       #mode[read=r,write=w.append=a]
#write file
fo.write("Hi!.......\n")
#write multiple line
line_list=["How are you? \n","How is the weather there? \n"]
fo.writelines(line_list)
#update file('a')
line_list=["It is really hot in Kolkata.\n","BTW how is your preparation for ISB going on\n","Are you attending the warm up session?\n"]
fo.writelines(line_list)

#open the first file in append mode
ff=open("E:\\example.txt",'a')

#open the second file in read mode
sf=open("E:\\Day1.txt",'r')

#read data from second file
info=sf.read()

#append the info data in the first file
ff.write(info)
#close both the files
ff.close()
sf.close()

