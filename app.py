import streamlit as st
from textblob import TextBlob
from better_profanity import profanity
import matplotlib.pyplot as plt

st.title("Mood2Emoji — Kid-Safe Text Mood Detector")
st.write("Type a sentence and see the emoji that matches the mood!")

user_input = st.text_input("Enter a sentence:")

def analyze_sentiment_with_filter(text):
    text = text.lower()
    profanity.load_censor_words()
    
    if profanity.contains_profanity(text):
        return "😐", "Let's use kind words!"
    
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    
    if sentiment > 0:
        return "😀", "Sounds happy!"
    elif sentiment < 0:
        return "😞", "Sounds upset."
    else:
        return "😐", "Neutral vibe!"


teacher_mode = st.checkbox("Teacher Mode - How this app works")

def create_sentiment_diagram():
    """Create a simple diagram showing how sentiment analysis works"""
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, 1)
    
    # Color areas
    ax.axvspan(-1, -0.1, alpha=0.3, color='red', label='Negative')
    ax.axvspan(-0.1, 0.1, alpha=0.3, color='gray', label='Neutral')
    ax.axvspan(0.1, 1, alpha=0.3, color='green', label='Positive')
    
    ax.set_xlabel('Sentiment Score (-1 to +1)')
    ax.set_title('How Mood2Emoji Works: Sentiment Analysis')
    ax.legend()
    
    return fig

if user_input:
    emoji, message = analyze_sentiment_with_filter(user_input)
    st.markdown(f"### {emoji} {message}")
    
    # Show sentiment score in Teacher Mode
    if teacher_mode and user_input.strip() and not profanity.contains_profanity(user_input.lower()):
        blob = TextBlob(user_input)
        sentiment_score = blob.sentiment.polarity
        st.write(f"**Sentiment Score:** {sentiment_score:.2f}")
        
        # Show the diagram
        st.write("### How It Works:")
        
        fig = create_sentiment_diagram()
        st.pyplot(fig)
        
        st.write(f"""
                 **Behind the scenes:**
                 - First, we **take the text** typed by the student  
                 - We convert everything to **lowercase** so the computer reads it easily  
                 - We use **Better Profanity** to check if the text contains bad or unsafe words  
                   - If yes → We block it and show a neutral emoji 😐  
                 - If the text is clean
                   - We send it to **TextBlob**, a Natural Language Processing (NLP) tool  
                 - TextBlob analyzes:
                   - Words with positive feelings → + score 😊  
                   - Words with negative feelings → – score 😢  
                   - Mixed or unclear → neutral 😐
                 - Based on the score:
                   - Score > 0 → 😀 Happy!
                   - Score = 0 → 😐 Neutral
                   - Score < 0 → 😞 Sad

                This is how computers **understand emotions** from plain text!
            """)

# Show info in Teacher Mode even without input
if teacher_mode and not user_input:
    st.info("**Teacher Mode Active** - Enter text to see sentiment analysis details!")
    fig = create_sentiment_diagram()
    st.pyplot(fig)