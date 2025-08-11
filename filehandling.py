f = open('poem1.txt','r')
print(f.read())
print("lines:",f.count('\n')+1)

f1 = open('abc.txt','w')
f1.write('yashi')


f1 = open('abc.txt','a')
f1.write("\nfuck you bitch")

#To copy contents of one file to other. While copying a) all full
# stops are to be replaced with commas b) lower case are to be replaced 
#with upper case c) upper case are to be replaced with lower case.


