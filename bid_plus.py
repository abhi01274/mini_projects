"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
      
      
      //*[@id="pagi_content"]/div[1]/div[1]/p[1]
      //*[@id="pagi_content"]/div[2]/div[1]/p[1]
      //*[@id="pagi_content"]/div[3]/div[1]/p[1]
      //*[@id="pagi_content"]/div[3]/div[1]/p[1]
      
"""
import csv
from  selenium import webdriver
from time import sleep
#url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"
url = "https://bidplus.gem.gov.in/bidlists"

browser = webdriver.Chrome("D:/forsk/selenium/chromedriver_win32/chromedriver.exe")
browser.get(url)


bids=[]
items1=[]



for i in range(1,5):
    bid_no = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]')
    bid_no.click()
    
    bids.append(bid_no.text)
    
    path_items='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[2]/p[1]/span'''
    items=browser.find_element_by_xpath(path_items).text
    items1.append(items)
    

sleep(6)


browser.quit()




with open("bid_plus.csv","r+") as file:
    write=csv.writer(file,delimiter=",")
    write.writerow(["BID NO","Items"])
    for i in range(len(bids)):
        tmp_lst = [bids[i],items[i]]
        for i in range(len(tmp_lst)):
            tmp_lst[i] = tmp_lst[i].replace("\n"," ")
        write.writerow(tmp_lst)


