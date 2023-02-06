# Welcome to Team 3's Data Science Industry Project

This repository is about the project we are currently working on is "Tweets Sentiment Analysis Application using Twitter API".

## Project scope

The aim of this project is to build an application that is capable of fast, real-time sentiment analysis of tweets with regards to the important conflict currently happening in Ukraine between Ukraine and Russia. The scope might cover anything between the energy crisis cause by the war to the world relations between states, especially the two currently implicated in the military confilct.

## Structure

This project is made up of two main stages:

 - the data pipeline that uses the Twitter API to extract, transform and load the data
 - the App that will generate real-time sentiment scores for the selected criteria
 
## Work distribution

Darius
- Finish sentiment analysis
- Clean ipynb file

Danko
- Stream current (daily) data from Twitter API to the app in the correct format

Balazs
- Put it all on github

Catalin
- Create sentiment prediction model for Ukraine and Russia

Danilo
- Make it into a WebApplication

## Features

1. Daily tweets related to Ukraine-Russia War
2. Summarise today's tweets
3. Daily sentiment for Ukraine and for Russia
4. Predict the sentiment for the next (7?) days

# Team Members

Alexandru Balazs
Danilo Vuita
Danko Mikic
Darius Cocirta
Catalin Iusan


# Project setup:

## Create the predict model:
- Install the following models using the commands: ’ !pip install prophet’ and
’ !pip install mxnet gluonts ujson’
- Run the ’prediction.ipynb’ as as a Google Collab file
## Web scrape python analysis:
- Import the related libraries
- Run the ’Big_Chungus.ipynb’ on any IDE that supports python (Visual Studio Code,
Pycharm, etc.)
## Web application:
- Import the ’APISetup’ folder as a Django project and run it accordingly


