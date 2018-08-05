# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 21:20:54 2018

@author: tammy_000
"""

import requests
from bs4 import BeautifulSoup
import tkinter
import webbrowser
#################GEt data from web
# specify the url
# query the website and return the html to the variable ‘page’
#==============================================================================
# TECH enw from bbc
#==============================================================================
storeurl = "https://www.bbc.com/news/technology"
page = requests.get(storeurl)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page.content, "html.parser")

#print out the result of the desired web content
price_box = soup.find("span", attrs={"class":"title-link__title-text"})

result1 = price_box.text
################REDIRECT TO SITE
def callback(event):
    #webbrowser.open_new(r"https://www.bbc.com/news/technology")
    webbrowser.open_new(storeurl) 
    
    
#==============================================================================
# TECH enw from NY times
#==============================================================================
storeurl2 = "https://webcat.hkpl.gov.hk/wicket/bookmarkable/com.vtls.chamo.webapp.component.patron.PatronAccountPage?0&theme=WEB&locale=en"
page2 = requests.get(storeurl2, auth=
('23838021295296', '8838'))


# parse the html using beautiful soup and store in variable `soup`
soup2 = BeautifulSoup(page2.content, "html.parser")

#print out the result of the desired web content
price_box2 = soup2.find("tr", attrs={"class":"even"})

result2 = price_box2.text
################REDIRECT TO SITE
def callback2(event):
    #webbrowser.open_new(r"https://www.bbc.com/news/technology")
    webbrowser.open_new(storeurl2) 
    #open a new pop up window

#open a new pop up window
root = tkinter.Tk()
root.wm_title("Today's Tech headlines")
#create a new entery box
label =tkinter.Label(root,text=result1 , fg="blue", cursor="hand2" )
label.pack()
label.bind("<Button-1>", callback)

label =tkinter.Label(root,text=result2 , fg="green", cursor="hand2" )
label.pack()
label.bind("<Button-1>", callback2)

root.mainloop()

