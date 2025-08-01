# Sentiment Analysis of Amazon Product Reviews

A lightweight web app to analyze product review sentiment using Naive Bayes and NLP techniques like tokenization, stopword removal, stemming, and TF-IDF vectorization.

[![Live Demo](https://img.shields.io/badge/🚀_Try_App-Click_Here-success?style=for-the-badge)](https://huggingface.co/spaces/HarshitaSuri/SentimentAnalysis)

---

## 🔗 Project Links

[![Colab](https://img.shields.io/badge/📓_Colab_Notebook-Open-blue?style=for-the-badge)](https://colab.research.google.com/drive/1HmNJ3EeoVdi8Ax0-EGD3sxFeOV4t76F5?usp=sharing)

[![Dataset](https://img.shields.io/badge/📁_Kaggle_Dataset-View-orange?style=for-the-badge)](https://www.kaggle.com/datasets/arhamrumi/amazon-product-reviews)


---

## 📌 Features

- Classifies product reviews as **Positive**, **Neutral**, or **Negative**
- Animated emoji burst from the bottom of the screen based on sentiment
- Preprocessing:  
  - ✅ Tokenization  
  - ✅ Stopword removal  
  - ✅ Stemming  
  - ✅ TF-IDF vectorization
- Built using **Naive Bayes classifier**
- Balanced dataset via downsampling
- Frontend made using **Gradio**, hosted on **Hugging Face Spaces**

---

## 🛠 Tech Stack

- Python  
- Scikit-learn  
- NLTK  
- Gradio  
- HTML + CSS (for emoji animation)

---

## 💬 Example Review Predictions

| Review                                 | Predicted Sentiment | Emoji Animation         |
|----------------------------------------|----------------------|--------------------------|
| "Absolutely loved it!"                 | Positive             | 🎉✨😍🥳                   |
| "It's okay, nothing special."          | Neutral              | 😐🤔🫤                    |
| "Worst purchase ever, waste of money"  | Negative             | 😡💩😭💔                   |

---

## 📁 Dataset Details

- Source: [Kaggle - arhamrumi/amazon-product-reviews](https://www.kaggle.com/datasets/arhamrumi/amazon-product-reviews)
- Total Reviews: ~275,000  
- Labels:
  - 1–2 stars → Negative  
  - 3 stars → Neutral  
  - 4–5 stars → Positive  
- Balanced: Upsampled to equal samples in each class
- Preprocessed using tokenization, stopword removal, stemming, and TF-IDF

---

## 🚀 How to Use

1. Type your product review into the textbox  
2. Submit it  
3. View the predicted sentiment  
4. Watch emojis burst based on the mood 🎉

---

👩‍💻 Developed by **Harshita Suri**
