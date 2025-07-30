# 🧠 Sentiment Analysis of Amazon Product Reviews with Emoji Animation

This web app predicts the sentiment of product reviews as **positive**, **neutral**, or **negative**, and displays an animated emoji burst to match the emotion.

---

## 🔗 Quick Access

👉 **[🚀 Try the Live App](https://huggingface.co/spaces/HarshitaSuri/SentimentAnalysis)**  
📓 **[🧾 View Training Notebook (Colab)](https://colab.research.google.com/drive/1HmNJ3EeoVdi8Ax0-EGD3sxFeOV4t76F5?usp=sharing)**  
📂 **[📁 Dataset on Kaggle](https://www.kaggle.com/datasets/arhamrumi/amazon-product-reviews)**

---

## 📌 Features

- ✅ Predicts sentiment: Positive, Neutral, or Negative
- ✅ Emoji animation based on the prediction result
- ✅ Built using a **Naive Bayes classifier**
- ✅ NLP preprocessing pipeline:
  - Tokenization
  - Stopword removal
  - Stemming
  - TF-IDF vectorization
- ✅ Balanced dataset using downsampling
- ✅ Web app built with Gradio and deployed on Hugging Face Spaces

---

## 🛠 Tech Stack

- **Python**
- **Scikit-learn** – Naive Bayes model
- **NLTK** – Tokenization, Stopword Removal, Stemming
- **TF-IDF Vectorizer** – Feature extraction
- **Gradio** – Web interface
- **HTML & CSS** – Custom emoji animation

---

## 💬 Example Review Predictions

| Review                                 | Predicted Sentiment | Emoji Animation         |
|----------------------------------------|----------------------|--------------------------|
| `"Absolutely loved it!"`               | Positive             | 🎉✨😍🥳                   |
| `"It's okay, nothing special."`        | Neutral              | 😐🤔🫤                    |
| `"Worst purchase ever, waste of money"`| Negative             | 😡💩😭💔                   |

---

## 📁 Dataset Details

- **Source**: [Kaggle - arhamrumi/amazon-product-reviews](https://www.kaggle.com/datasets/arhamrumi/amazon-product-reviews)
- **Reviews**: ~275,000
- **Labels**: Derived from star ratings and grouped as:
  - 1–2 stars → Negative  
  - 3 stars → Neutral  
  - 4–5 stars → Positive
- **Preprocessing**:
  - Tokenization of review text
  - Stopword removal
  - Stemming using NLTK
  - Feature transformation via TF-IDF
- **Balancing**: Downsampled to equalize class sizes

---

## 🚀 How to Use

1. Enter any product-style review in the textbox  
2. Click **Submit**  
3. View the sentiment prediction  
4. Watch emojis burst from the bottom of your screen based on the sentiment 🎉

---

> 👩‍💻 Developed by **Harshita Suri** as an NLP + ML project combining prediction and visual interaction
