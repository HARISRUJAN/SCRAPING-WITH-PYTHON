import scrapy
from bs4 import BeautifulSoup
import requests
from ..items import SihItem
class simple(scrapy.Spider):
              name='implication1'
              start_urls=["http://mits.ac.in"]
              def parse(self,response):
                           items=SihItem()
                           r = requests.get("http://mits.ac.in")
                           soup = BeautifulSoup(r.content)
                           l=[]
                           for tag in soup.find_all():
                              l.append(tag.name);
                           l= list(dict.fromkeys(l))
                           print("this is L",l)          
                           #for q1 in response.css('body'):
                           for tag in l:
                               s='//';
                               s=s+tag;
                               s=s+'/text()';
                               h=response.xpath(s).extract();
                              # items['tag']=tag;
                              # items['data']=h;
                               yield items
                           items["URL"]="Moving to nextpage"
                           items["Country"]="Moving to nextpage"
                           yield items;
                           #next_page=response.css("a::attr('href')").get()
                           #print("this is nextpage",next_page)
                           #if next_page is not Nonew:
