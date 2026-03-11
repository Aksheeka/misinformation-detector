# AI Misinformation Pattern Analyzer

## Overview

This project is a simple web application that analyzes headlines or short pieces of text and identifies patterns commonly found in misleading or sensational content.

The goal of the project is to explore how basic Natural Language Processing (NLP) and machine learning techniques can help detect signals that are often present in misinformation.

Instead of trying to prove whether a statement is true or false, the tool highlights potential warning signs such as emotional language or sensational phrases.

---

## How the Project Works

The system evaluates the input text using three simple checks.

### 1. Sentiment Analysis

The emotional tone of the text is analyzed using TextBlob.  
Highly emotional headlines are often used in misleading or clickbait content.

Example:

Shocking discovery doctors don't want you to know!

The system flags headlines with extreme positive or negative sentiment.

---

### 2. Sensational Phrase Detection

The program checks for phrases that are commonly used in exaggerated or manipulative headlines.

Examples include:

- shocking
- secret
- exposed
- breaking
- miracle cure
- hidden truth

Each detected phrase increases the risk score.

---

### 3. Machine Learning Classification

A simple Logistic Regression model is trained on a small set of example headlines labeled as either:

- credible
- potentially misleading

The model converts text into numerical features using CountVectorizer and predicts whether the input resembles misleading headlines.

---

## Output

After analyzing the text, the system returns:

- Sentiment score
- Number of sensational phrases detected
- Overall credibility risk

Possible results:

- Low Risk
- Moderate Risk
- High Risk of Misinformation

---

## Technologies Used

Python – core programming language  
Flask – web framework used to create the web interface  
TextBlob – used for sentiment analysis  
Scikit-learn – used for machine learning (vectorization and classification)

---

## Project Structure

```
misinformation-detector/
│
├── app.py
├── model.py
├── requirements.txt
│
└── templates/
    └── index.html
```

---

## Running the Project

Install dependencies:

```
pip install flask textblob scikit-learn
python -m textblob.download_corpora
```

Run the application:

```
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## Example Input

Scientists reveal shocking secret that will change everything!

Example Output

Sentiment Score: 0.65  
Sensational Words Detected: 2  
Credibility Risk: Moderate Risk

---

## Limitations

This project is a simple prototype built for learning purposes.  
It works best on headlines or short text and does not perform full fact-checking.

Future improvements could include:

- larger training datasets
- source credibility analysis
- more advanced NLP models

---

## Purpose of the Project

This project was created to explore how simple AI tools can be used to analyze information patterns in online media and encourage more responsible consumption of digital content.
