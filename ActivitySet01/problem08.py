# Files

#filename = "dataset/mbox-short.txt"
#word='reva'
#count =0
#for letter in word:
  #if letter == 'a':
   #count=count+1
#print(count) 
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
      continue
 ab=float(line.find("0"))
        print(ab)
        count=count+1
        total=total+ab
average=total/count
print("Average spam confidence: ",average)