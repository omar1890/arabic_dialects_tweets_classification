# arabic_dialects_tweets_classification

This project consists of the following steps :
## Step 1 : 
- I have a *file1 with dataset contains ID and Target classes of arabic dialects (18) 
- I need to scrape the text of tweets from specific API with ID from *file1
- Merge two files based on IDs and apply some EDA 
- Save merged files into one file *file2
## Step 2 :
- Read *file2
- Some EDA to decide which steps to keep in mind during preprocessing
- Preprocessing tweets with regex and other techniques
- Apply Stemming and (try to apply lemmitiaztion- Not yet)
- Save cleaned data  *file3 

## Step 3 :
- Read cleaned data *file3
- Try to remove stopwords 
- Apply the following techinques 
      - Count Vectorizer 
      - TFIDF
- Apply the following models :
      - Support vector for classification  *model1
      - Naive Bayes for multinomial *model2
      - Neural Network *model3
## Step 4 :
- Save the best model which is *model2 with <strong> accuracy 55.4% </strong>
- Build html page with a form for text 
![image](https://user-images.githubusercontent.com/19292752/158206965-038f8c49-c415-4910-bd72-1b47bc1c4410.png)

- Deployment with flask 

## Conclosion :
- applying stemming is not the best (by make a quick comparsion betweent columns and also the accuracy) 
- removing stopwords affect good
- I think, I have made a good cleaning but it didn't reflect best in the accuracy 
## Future Work : 
- try to apply lemmitization 
- hyper parameter tuning for models 
- try tuning for Countvectorizer and TFIDF
- Try tree-based models like XGB
