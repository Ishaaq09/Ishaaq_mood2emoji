# Mood2Emoji — Kids’ Friendly Sentiment-to-Emoji App

---

Mood2Emoji is a fun and safe learning app that converts sentences into emojis based on **sentiment**.  
Kids type how they feel → the app responds with a mood emoji!

1. Simple  
2. Educational  
3. Safe (Profanity Filter Included)

## Purpose of the Project

This project introduces young learners to **Natural Language Processing (NLP)** through a playful activity.

Kids learn:
- What *sentiment* means (positive, negative, neutral)
- How computers understand text using AI
- How emojis can express emotions
- How responsible AI filters harmful words

The goal is to bridge **technology + emotional learning** in a fun way.

## App Demo (Screenshot Placeholder)

*(Add screenshot here)*  
`![App Screenshot](assets/screenshot.png)`

## How to Install & Run

### Requirements
Install dependencies:

```bash
pip install streamlit textblob better_profanity
python -m textblob.download_corpora
```
### Run the App

```bash
streamlit run app.py
```
Then visit the local URL shown in your terminal
Usually:
```
http://localhost:8501
```

## How It Works (Teacher Mode)

| Feature | Purpose |
|--------|---------|
| **TextBlob Sentiment Analysis** | Detects if a sentence is positive, negative, or neutral |
| **Emoji Mapping** | Converts mood polarity into a clear emoji |
| **Profanity Filter** | Hides disrespectful words to keep learning safe |
| **Friendly Feedback Messages** | Helps kids understand emotional context |

#### Simple Behind-the-Scenes Logic
1. Clean the sentence → check for bad words
2. Convert words into a **polarity score**
3. Display the corresponding emoji:
   - Score > 0 → 😀 Happy
   - Score < 0 → 😞 Sad
   - Score = 0 → 😐 Neutral

## How to Teach This in 60 Minutes

| Time | Activity |
|------|----------|
| 0–10 min | Introduce emotions → *How do we show feelings using emojis?* |
| 10–20 min | Explain sentiment (positive/negative/neutral examples) |
| 20–30 min | Introduce AI & TextBlob in simple terms |
| 30–45 min | Kids try the Mood2Emoji app (hands-on demo) |
| 45–55 min | Talk about **digital kindness** and safe language |
| 55–60 min | Group reflection & Q&A |

No coding skills required  
Interactive learning experience

## Learning Outcomes

After the session, students will:
- Understand **what sentiment is**
- Know emojis help show **emotions**
- See how AI **analyzes mood** from text
- Recognize technology should be **kind and safe**
- Experiment with emotional expressions in sentences

### Known Limitations

| Limitation | Details |
|-----------|---------|
| Basic emotion categories | Only 3 emojis (happy/sad/neutral) |
| Accuracy | Simple sentiment model may misunderstand sarcasm or context |
| No semantic understanding | The model does not understand deeper meaning — only counts word polarity |
| Language restriction | Works best only in English |
| Short text behavior | Very small sentences may show neutral results |

## Possible Future Enhancements
- Support for more diverse emojis 
- Multi-language support 
- Cloud deployment for public access 
- Understanding complex tone like sarcasm 
