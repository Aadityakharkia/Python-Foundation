a= input("Please enter a sentence ")
a= a.strip()
l = len(a)
c = 0 
for i in range(0,l):
    if (a[i]==' ' and a[i+1]!=' '):
            c=c+1
print(" Number of vowels a in the sentence ",a, "is",c)