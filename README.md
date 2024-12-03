# Amazon Product Reviewer
### This is a program that can take URLs of amazon products, look through some of the reviews, and return a graph of the found data.
## 1. Installing the Software
1. Download Conda [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).
2. Use the attached yaml file to recreate the environment(`conda env create -f Amazon_Reviewer.yaml`).
3. Make sure you have a local Phi-3.gguf file downloaded ( ex: Phi-3-mini-4k-instruct-fp16.gguf), or you could use another LLM compatible with the llamacpp python library.
   -If you do use a different LLM make sure to update the code on lines 25 and 26.
4. Make sure you have google chrome downloaded, as this program uses Selenium to open google chrome and webscrape data from Amazon.

## 2. Preparing the Input URLs
1. Go to Amazon and find products you would like to compare.
![image](https://github.com/user-attachments/assets/43b98d4b-558f-48c6-8d87-bbae8c0037ae)

3. Compile the URLs of these products into an input File each separated on a different line (see InputURLS.txt).

## 3. Running the Software
1. At this point, you can have the software do the rest of the work.
2. During this process two different types of files will be generated
   -(Product Name).txt files will contain the reviews scraped from Amazon
   -Sentiments_(Product Name).txt files will contain a list of sentiments that correspond to each review and whether or not it was positive, neutral, or negative
3. When the program is finished, a graph of the data created using matplotlib and numpy will appear similarly to the one pictured below.
![image](https://github.com/user-attachments/assets/23f7d5bd-3143-4eb2-9f4e-14343be88c53)

