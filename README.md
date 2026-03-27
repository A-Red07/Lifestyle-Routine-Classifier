# Lifestyle-Routine-Classifier
AI Daily Routine Analyzer
Project Overview

The AI Daily Routine Analyzer is a machine learning project that analyzes a person's daily habits and predicts whether their routine is Good, Average, or Poor. The system uses a Decision Tree Classifier to learn patterns from routine data and provide suggestions for improving lifestyle habits.

Features
Predicts routine quality (Good / Average / Poor)
Uses Decision Tree Machine Learning algorithm
Takes user input for daily habits
Validates user input ranges
Provides personalized suggestions
Simple and interactive command line interface
Technologies Used
Python
Pandas
Scikit-learn
Machine Learning (Decision Tree Classifier)
Input Parameters

The model takes the following inputs:

Sleep hours
Water intake (glasses)
Exercise minutes
Screen time (hours)
Study hours
Meals per day
Wake up early (Yes/No)
Output

The system predicts:

Good Routine
Average Routine
Poor Routine

And provides suggestions for improvement.

Machine Learning Model

This project uses a Decision Tree Classifier which is a supervised machine learning algorithm used for classification problems. The model is trained on routine data and learns patterns between lifestyle habits and routine quality.

How to Run
Install Python
Install required libraries:
pip install pandas scikit-learn
Run the Python file:
python routine_analyzer.py
Future Improvements
Add GUI interface
Use larger dataset
Add data visualization
Deploy as web app
Improve model accuracy
