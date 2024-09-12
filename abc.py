print("hello world")
#Reverse a string
s = "i.like.this.program.very.much"
s = s.split(".")
i,j =  0, len(s)-1
while(i<=j):
    s[i],s[j] = s[j],s[i]
    i,j = i+1, j-1
print(".".join(s))