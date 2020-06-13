import scrapy
import sys
import string
import urllib
from urllib.request import urlopen
from urllib.parse import urlparse
import socket
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from ..items import SihItem
class simple(scrapy.Spider):
              name='implication1'
              i=0;
              start_urls=["https://www.sih.gov.in"]
              def parse(self,response):
               items=SihItem()
               e=""
               a=self.start_urls[self.i]
               j=len(self.start_urls[self.i])-1
               k=0
               flag=0
               while(k<=j):
                k=k+1
                if(a[k-1]=='/'):
                  flag=flag+1
                  continue;
                if(flag>=2 and flag<3):
                 e=e+a[k-1]
                if(flag==3):
                  break;
               a=e

               s=response.xpath("//title/text()").extract()
               now=datetime.now()
               cs=now.strftime("%d/%m/%y %H:%M:%S")
               items["Time"]=cs
               try:
                items["IP_Address"]=socket.gethostbyname(a)
                w=socket.gethostbyname(a)
                ress=urllib.request.urlopen("http://api.hostip.info/get_html.php?ip={}&position=true".format(w)).read()
                
                items["Country"]=ress

               except:
                items["URL"]=self.start_urls[self.i]

               
        
               items["Snippet"]=s
               self.i=self.i+1
               yield items;
                           
                           
               next_page=response.xpath("//a/@href").extract()
                          
               if next_page is not None:

                for r1 in next_page:
                 self.start_urls.append(r1)
                 yield response.follow(r1,callback=self.parse)                     #print("this is nextpage",next_page)
                           #if next_page is not None
