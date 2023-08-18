## Crawler of the Diário Oficial do Estado de Roraima
- url https://www.imprensaoficial.rr.gov.br/app/_inicial/
- Implemented for the exclusive structure of this website and limited to 2023 posts
- Used of scrapy, nltk, PyPDF2, NPL

## Problems encountered during development
- There was no kind of url exclusive for the PDF to be found, it had to be acquired through a POST
- The params nedeed for the POST request were hidden
- The PDF itself was in an <embed> element because of a chrome extension in the html, neutralizing the use of JavaScript to get the pdf text


## Future implementation
- This project has some limitations (it's just for example) like the time of execution, it will crawl the same page/pdfs every time that it runs, tokenized word that are not completed
- To solve this problems the solutions will be implement a more detailed and organized application like improve the natural processing language, save in a DB the name of the last file that was crawled to avoid all the unnecessary process
- It also will be implemented in a Docker environment

- ## Tutorial for run the project
- Go to diario_oficial_crawler
- Inside the project paste this command in terminal: scrapy crawl myCrawler -o ouput.json
- See the "pdfs" folder, it contains the top 10 words (tokenized) of the file
- See the output.json (if you let the crawler finish) that will contain all the pdfs that was crawled
- (OBS: Watch-out for the number of files it's gonna generate inside the  "pdfs" folder, this project does not contain a limit for the files)
