# Experiments-with-Machine-Learning-

##Description:
Use scikit-learn  machine  learning  framework  to experiment with two different machine learning algorithms using sentiment data set
Use a collection of customer reviews from six of the review topics.
-Data preprocessing + split the data into a training and an evaluation part
* Plot the distribution of the number of the instances in each class.
* Run 3 different ML models: 
a) Naive Bayes Classifier 
b) Base-DT: a baseline Decision Tree using entropy as decision criterion and using default values for the rest of the parameters. 
c) Best-DT: a better performing Decision Tree
* Error Analysis

## Team Members
Karl-Joey Chami *27736657*
Michel Abboud *40025378*
Adrian Patterson *40048841*
Khalil Nijaoui *40092653*

## Requirements
This assignment uses Jupyter Notebook, an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text.

## Local Run

 - Download and install Anaconda Individual Edition from https://www.anaconda.com/products/individual
 - After installation, run Anaconda Prompt (Anaconda3)
 - Navigate to the directory where the *.ipynb* file resides
 - Type in `jupyter notebook` in the command prompt
 - Jupyter Notebook will open up on your default browser
	 - Click on File, Open
	 - Choose the file *Assignment1_comp472.ipynb*
	 - Click on Kernel, Restart and Run all

## Important Notes

 - Make sure *all_sentiment_shuffled.txt* text file is in the same directory as *Assignment1_comp472.ipynb*
 
## Troubleshooting Issues
* The most likely issue is a missing library

### NLTK not Found
* The **NLTK** Library does *not* come installed with Anaconda
* Visit the [NLTK Installation Page](https://www.nltk.org/install.html)
* What is NLTK?
    * NLTK is a **N**atural **L**anguage **P**rocessing **T**oolkit
    * NLTK has functions to help us clean our text and remove unnecessary words/punctuation
