# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:09:15 2020

@author: Kevin
"""

import PyPDF2


russell3000MembersFile="RU3000_MembershipList_20190701.pdf"
f=open(russell3000MembersFile,"rb")
pdfReader=PyPDF2.PdfFileReader(f)
numPages=pdfReader.getNumPages()
compPlusTickers=[]
companies=[]
tickers=[]
for j in range(0,numPages-1):
    pageObj=pdfReader.getPage(j)
    pageText=pageObj.extractText()
    pageTextSplit=pageText.split("\n")
    for n,i in enumerate(pageTextSplit):
        if (i=="Company" or i=="Ticker" or i=="Membership list" 
            or i=="Russell US Indexes" or i=="July 01, 2019"
            or i==str(j+1) or i=="" or i=="ftserussell.com"):
            continue
        elif (n%2)==0:
            i=i.strip()
            companies.append(i)
        elif (n%2)!=0:
            i=i.strip()
            tickers.append(i)

    
    
