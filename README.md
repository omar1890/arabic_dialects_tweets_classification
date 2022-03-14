# arabic_dialects_tweets_classification

This project consists of the following steps :
## Step 1 : <a href='https://github.com/omar1890/arabic_dialects_tweets_classification/blob/master/01_fetch_data.ipynb'>01_fetch_data notebook</a>
- I have a *file1 with dataset contains ID and Target classes of arabic dialects (18) 
- I need to scrape the text of tweets from specific API with ID from *file1
- Merge two files based on IDs and apply some EDA 
- Save merged files into one file *file2
## Step 2 : <a href='https://github.com/omar1890/arabic_dialects_tweets_classification/blob/master/02_preprocessing_data.ipynb'>02_preprocessing_data notebook</a>
- Read *file2
- Some EDA to decide which steps to keep in mind during preprocessing
- Preprocessing tweets with regex and other techniques
- Apply Stemming and (try to apply lemmitiaztion- Not yet)
- Save cleaned data  *file3 

## Step 3 : <a href='https://github.com/omar1890/arabic_dialects_tweets_classification/blob/master/03_modeling.ipynb'>03_modeling notebook</a>
- Read cleaned data *file3
- Try to remove stopwords 
- Apply the following techinques 
      - Count Vectorizer 
      - TFIDF
- Apply the following models :
      - Support vector for classification  *model1
      - Naive Bayes for multinomial *model2
      - Neural Network *model3
## Step 4 : <a href='https://github.com/omar1890/arabic_dialects_tweets_classification/blob/master/04_deployment.py'>04_deployment notebook</a>
- Save the best model which is *model2 with <strong> accuracy 55.4% </strong>
- Build html page with a form for text 
![image](https://user-images.githubusercontent.com/19292752/158206965-038f8c49-c415-4910-bd72-1b47bc1c4410.png)
<a href='https://github.com/omar1890/arabic_dialects_tweets_classification/tree/master/templates/home.html'>home html</a>

- Deployment with flask 

## Conclosion :
- applying stemming is not the best (by make a quick comparsion betweent columns and also the accuracy) 
- removing stopwords affect good
- I think, I have made a good cleaning but it didn't reflect best in the accuracy 
- I couldn't apply NN since I have a limit resources but I think after tuning it may get best result
## Future Work : 
- try to apply lemmitization 
- hyper parameter tuning for models 
- try tuning for Countvectorizer and TFIDF
- Try tree-based models like XGB
- Try to apply NN well
- Build a dashboard with visualization

# Note: You can find used resources through notebooks
