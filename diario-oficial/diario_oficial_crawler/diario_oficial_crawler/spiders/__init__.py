import string

from scrapy.spiders import CrawlSpider, Rule
import requests
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from scrapy.linkextractors import LinkExtractor
from PyPDF2 import PdfReader
from collections import Counter
import io
from contextlib import redirect_stdout
import os

nltk.download('punkt')
nltk.download('stopwords')


# For this example I will be using only 2023 files and pages. Later can be implemented a crawler for the entire site
class CrawlSpiderExample(CrawlSpider):
    name = "myCrawler"
    start_urls = ["https://www.imprensaoficial.rr.gov.br/app/"]
    rules = ([
        Rule(LinkExtractor(allow=r"_visualizar-mes/"), callback='parse_item')
    ])

    def parse_item(self, response):
        table_row = response.css("tbody")
        for row in table_row:
            item = {
                'doe': row.css("form > input[type=hidden][name=doe]::attr(value)").get(),
                'ipconexao': row.css("form > input[type=hidden][name=ipconexao]::attr(value)").get(),
                'dia': row.css("form > input[type=hidden][name=dia]::attr(value)").get(),
                'mes': row.css("form > input[type=hidden][name=mes]::attr(value)").get(),
                'ano': row.css("form > input[type=hidden][name=ano]::attr(value)").get(),
                'hora': row.css("form > input[type=hidden][name=hora]::attr(value)").get()
            }
            yield item['doe']
            self.get_pdf(item)

    def get_pdf(self, item):
        url = "https://www.imprensaoficial.rr.gov.br/app/_visualizar-doe/"
        files = [

        ]
        headers = {}
        pdf_data_raw = requests.request("POST", url, headers=headers, data=item, files=files).content
        self.map_pdf_words(pdf_data_raw, item)

    def map_pdf_words(self, pdf_data_raw, item):
        with io.BytesIO(pdf_data_raw) as open_pdf_file:
            reader = PdfReader(open_pdf_file)
            num_pages = len(reader.pages)
            print(f"This file has {num_pages} number of pages")
            # Extract text from each page of the PDF
            pdf_text = ''
            for page_num in range(len(reader.pages)):
                pdf_text += reader.pages[page_num].extract_text()
                # Convert into tokens to lowercase and remove stopwords and punctuation
                tokens = word_tokenize(pdf_text)
                stop_words = set(stopwords.words('portuguese'))
                filtered_tokens = [word.lower() for word in tokens if
                                   word.isalpha() and word.lower() not in stop_words and word not in string.punctuation]
                # Calculate word frequency and Display the most common keywords
                word_frequency = Counter(filtered_tokens)
                num_keywords = 50
                most_common_keywords = word_frequency.most_common(num_keywords)
                file_name = item["doe"][8:20]
                with open(f'{os.path.abspath(os.curdir)}/pdfs/{file_name}.txt', 'w') as f:
                    for keyword, frequency in most_common_keywords:
                        with redirect_stdout(f):
                            print(keyword, frequency)
