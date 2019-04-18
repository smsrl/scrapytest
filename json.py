
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)import json
website_string =' ' '
{
"website": [

{
         "logo url":"<img class="lazy"                  src="https://d3gecv9w1cv0iw.cloudfront.net/image/160/138/3039.do" data-                 original="https://d3gecv9w1cv0iw.cloudfront.net/image/160/138/3039.do" alt="Intl                 Trade On The Internet in United States" itemprop="image" style="display: inline;">",
          "title":"International Inernet Strategies",
          "subtitle":"Intl Trade On The Internet, United States",
          "Primary location": "New york,United States",
          "Area of expertise":"Starting In Import/Export in the United States",
           "About":"	Since 1995 BARNEY LEHRER has been a pioneer and leader in the            world of online international B2B information and commerce. He made the fita.org            site a preeminent portal on the web for resources and information about international            trade and for many years has been editing and distributing FITA’s bi-weekly            newsletter “Really Useful Resources for International Trade Professionals”             (http://reallyusefulsites.com).  He also was instrumental in the development of            GlobalTrade.net .Mr. Lehrer is a recognized consultant for international B2B online            trade and commerce. His clients include trading companies, exporters and            government agencies worldwide.",
           "Website":"http:// International Inernet Strategies.com",
           "Language spoken":" English",

           "Page url": "https://www.globaltrade.net/international-trade-import-exports/expert-            service-provider-p/Bar   ney-Lehrer-2.html?            currentSpId=5452&fromUrl=spb93cab9a9e761e4d4b7898e37e17cdb40a97a4579"

   
       
  },
  {
           "logo url":"<img class="lazy"      src="https://d3gecv9w1cv0iw.cloudfront.net/image/160/138/3039.do" data-     original="https://d3gecv9w1cv0iw.cloudfront.net/image/160/138/3039.do" alt="Intl Trade      On The Internet in United States" itemprop="image" style="display: inline;">",
     "title":"International Inernet Strategies",
     "subtitle":"Intl Trade On The Internet, United States",
     
"Primary location": "New york,United States",
"Area of expertise":"Starting In Import/Export in the United States",
"About":"	Since 1995 BARNEY LEHRER has been a pioneer and leader in the world of online international B2B information and commerce. He made the fita.org site a preeminent portal on the web for resources and information about international trade and for many years has been editing and distributing FITA’s bi-weekly newsletter “Really Useful Resources for International Trade Professionals”  (http://reallyusefulsites.com).  He also was instrumental in the development of GlobalTrade.net .Mr. Lehrer is a recognized consultant for international B2B online trade and commerce. His clients include trading companies, exporters and government agencies worldwide.",
"Website":"http:// International Inernet Strategies.com",
"Language spoken":" English",

"Page url": "https://www.globaltrade.net/international-trade-import-exports/expert-service-provider-p/Barney-Lehrer-2.html?currentSpId=5452&fromUrl=spb93cab9a9e761e4d4b7898e37e17cdb40a97a4579"

   }
  ]
}
' ' '
data = json.loads(website_string)
print(data)



















