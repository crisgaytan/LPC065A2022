import os

import requests
from lxml import html
from bs4 import BeautifulSoup

#import urlparsee

url=input("ingrese la pagina a revisar:")

class Scraping:
    
    
    def scrapingLinks(self,url):
            print("\nObteniendo links de la url:"+ url)
        
            try:
                response = requests.get(url)  
                parsed_body = html.fromstring(response.text)
    
                
                links = parsed_body.xpath('//a/@href')
    
                print('links %s encontrados' % len(links))
    
                for link in links:
                    print(link)
                    archivo= open("texto.txt","a")
                    archivo.write(link)
                    archivo.close()

                
            except Exception as e:
                    print(e)
                    print("Error conexion con " + url)
                    pass

scraping = Scraping()
scraping.scrapingLinks(url)
