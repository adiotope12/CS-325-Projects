from scrapper import *
from llama_cpp import Llama
import matplotlib.pyplot as plt
import numpy as np
#Represents the data of each item
class Item:
    def __init__ (self, fileName):
        self.fileName = fileName
        self.sentimentsFileName = "Sentiments_"+ fileName
        self.positive = 0
        self.neutral = 0
        self.negative = 0
        f = open(self.sentimentsFileName, "w+", encoding="utf-8")
        f.close
    
    #Adds respective sentiment to the sentiment file and to class member variable
    def AddPositive(self):
        self.positive += 1
        f = open(self.sentimentsFileName, "a", encoding="utf-8")
        f.write("Positive\n")
        f.close
    
    def AddNegative(self):
        self.negative += 1
        f = open(self.sentimentsFileName, "a", encoding="utf-8")
        f.write("Negative\n")
        f.close

    def AddNeutral(self):
        self.neutral += 1
        f = open(self.sentimentsFileName, "a", encoding="utf-8")
        f.write("Neutral\n")
        f.close

#Used to compile the prompt to send to the LLM
class Prompt:
    def __init__(self):
        self.prompt = "Tell me in one word is this statement positve, negative, or neutral : "
    def AddReview(self,curLine):
        self.prompt += curLine.strip()
    def ReturnReview(self):
        return self.prompt
    
#Class for obtining Sentiments
class Sentiments:
    def __init__(self,inputFileName):
        self.inputFileName = inputFileName
        self.sentimentFiles = []
    def FindSentiments(self):
        #Opens the inputFile with the URLs and begins to iterate through each product
        try:
            inputFile = open(self.inputFileName, "r", encoding="utf-8")
        except FileNotFoundError:
            print("Error Opening Input File : File was not found")
            return
        except:
            print("Error Opening Input File : ")
            return
        
        #Starts up the local LLM
        llm = Llama.from_pretrained(
            repo_id="microsoft/Phi-3-mini-4k-instruct-gguf",
            filename="Phi-3-mini-4k-instruct-fp16.gguf",
        )
        

        url = inputFile.readline()
        while (url != ""):
    
            curItem = Item(WebScrapper.GetReviews(url))
            if curItem.sentimentsFileName in self.sentimentFiles:
                url = inputFile.readline()
                continue

            #Opens the file with the review
            f = open(curItem.fileName, "r",encoding="utf-8")

            #Compiles each line of the review together 
            curLine = f.readline()
            while(curLine != ""):
                prompt = Prompt()
                #Gets line from review until the end, or word limit has been reached
                while((curLine != "-") and (len(prompt.ReturnReview().split(" ")) < 200)):
                    if(curLine != ""):
                        prompt.AddReview(curLine)
                    curLine = f.readline().strip()
                
                #Sends the prompt to the LLM
                temp = llm.create_chat_completion(
                    messages = [
                        {
                        "role": "user",
                        "content": str(prompt.ReturnReview())
                        }
                    ]	
                )

                #Gets and stores the response from the LLM
                response = temp["choices"][0]["message"]["content"].lower().strip()
                
                if "positive" in response:
                    curItem.AddPositive()
                elif "negative" in response:
                    curItem.AddNegative()
                elif "neutral" in response:
                    curItem.AddNeutral()

                #If review was cut off due  to size, then we skip through to the end of the review
                while(curLine != "-"):
                    curLine = f.readline().strip()

                curLine = f.readline().strip()

            self.sentimentFiles.append(curItem.sentimentsFileName)
            url = inputFile.readline()
    def ReturnSentiments(self):
        return self.sentimentFiles

#Used to compile the data from the Sentiment files and create the graph  
class Graph:
    def __init__(self, dataFiles : list):
        self.dataFiles = dataFiles
        #Represents the positve sentiments
        self.y1 = []
        #Represents the negative sentiments
        self.y2 = []
        #Represents the neutral sentiments
        self.y3 = []
    def GatherData(self):

        #Iterates through the list of files passed in and compiles the Sentiment data
        for File in self.dataFiles:
            f  = open(File,"r",encoding="utf-8")

            positive = 0
            negative = 0
            neutral = 0

            curLine = f.readline().strip()
            while (curLine != ""):
                match(curLine):
                    case "Positive":
                        positive += 1
                    case "Negative":
                        negative += 1
                    case "Neutral":
                        neutral += 1
                curLine = f.readline().strip()
                
            self.y1.append(positive)
            self.y2.append(negative)
            self.y3.append(neutral)
    def CreateGraph(self):
        if(self.y1 == [] and self.y2 == [] and self.y3 == []):
            print("There is no data to graph \n")
            return

        x = np.arange(len(self.dataFiles))  
        width = 0.2

        #Gets the item names from the name of their respective sentiment file
        itemNames = []
        for item in self.dataFiles:
            itemNames.append(item.split("_")[1].split(".")[0])
    
        # plot data in grouped manner of bar type 
        plt.subplots_adjust(left = .05, right = .95)
        plt.bar(x-0.2, self.y1, width, color='green') 
        plt.bar(x, self.y2, width, color='red') 
        plt.bar(x+0.2, self.y3, width, color='orange') 
        plt.xticks(x, itemNames) 
        plt.xlabel("Item") 
        plt.ylabel("Sentiments") 
        plt.legend(["Positive", "Negative", "Neutral"]) 
        plt.show()    

def main():
    sentimentFiles = Sentiments("InputURLS.txt")
    sentimentFiles.FindSentiments()
    graph = Graph(sentimentFiles.ReturnSentiments())
    graph.GatherData()
    graph.CreateGraph()

main()





