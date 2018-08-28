from bs4 import BeautifulSoup as soup
from urllib import urlopen as ureq
htmlfile=ureq("https://www.edureka.co/blog/interview-questions/python-interview-questions/")
htmltext=htmlfile.read()
htmlfile.close()
page_soup=soup(htmltext,"html.parser")
filename="rader1.txt"
f=open(filename,'w')



questions=page_soup.findAll("span",{"style":"font-family: verdana, geneva, sans-serif;"})

for question in questions:
	q=question.findAll("span",{"style":"font-family: verdana, geneva, sans-serif;"})
	k=q[0].text	
	#print(k)	
	f.write(k)

f.close()
