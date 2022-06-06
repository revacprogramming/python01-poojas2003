# Strings

#text = "X-DSPAM-Confidence:    0.8475"
text = "X-DSPAM-Confidence:    0.8475"
c=text.split()
a=text.find('0.8475')
print(float(text[a:]))

#fruit='banana'
#index=0
#  letter=fruit[index]
 # print(index,letter)
 # index=index+1