import scrapy
import spacy

class wiki(scrapy.Spider):
    name='wiki'
    start_urls =[
            #'https://en.wikipedia.org/wiki/Rambabu_Kodali'
            'https://en.wikipedia.org/wiki/Maulana_Azad_National_Institute_of_Technology'
    ]

    def parse(self,response):
        title=response.css("title::text").extract()
        href=response.css('a').xpath('@href').extract();
        yield {"TITLE_TEXT": title }
        yield {"links":href}
