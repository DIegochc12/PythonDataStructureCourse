text = "X-DSPAM-Confidence:    0.8475"
x=text.find(':')
ntext=text[x+1:]
num=float(ntext.lstrip())
print(num)
