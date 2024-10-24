# CS-325-Project 2
## This is a program used to web scrape reviews from Amazon products.
2. Use the included requirements.yaml file to recreate the environment
```(conda env  create -f requirements.yaml) ```.
4. Ensure that you have Google Chrome installed.
5. Add your product URLs to the inputURLS file, putting each URL on a separate line.
6. Before running the scrapper.py file, ensure that you have the correct file path to the inputURLS file in the scrapper.py program. Line 44 - ```inputFile = open("inputURLS.txt", "r", encoding="utf-8")```
7. Run the scrapper.py file, this program will iterate through the URLs in the inputURLs file and use Selenium to scrape the reviews of the inputed products.
 
