import pytest
from scrapper import *
from llama_cpp import Llama
import matplotlib.pyplot as plt
import numpy as np
from program import Sentiments,Graph,Prompt,Item

def test_empty_input_file():
  sentiment = Sentiments("")
  sentiment.FindSentiments()
  assert sentiment.ReturnSentiments() == []

def test_repeated_URLS():
  sentiment = Sentiments("TestCase2URLS.txt")
  sentiment.FindSentiments()
  assert len(sentiment.ReturnSentiments()) == 1

def test_too_large_review():
  sentiment = Sentiments("TestCase3URLS.txt")
  sentiment.FindSentiments()

  #Get number of sentimnents to make sure it matches the number of reviews
  f = open(sentiment.ReturnSentiments()[0], "r",encoding="utf-8")
  sentimentCount = 0
  curLine = f.readline()
  while(curLine != ""):
    sentimentCount += 1
    curLine = f.readline()

  assert sentimentCount == 11

def test_Invalid_Sentiments():
  graph = Graph(["TestCase4Sentiments.txt"])
  graph.GatherData()
  assert len(graph.y1) == 1 and len(graph.y2) == 1 and len(graph.y3) == 1
