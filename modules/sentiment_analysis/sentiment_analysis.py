from collections import Counter
from nltk.tokenize import sent_tokenize

def perform_sentiment_analysis(clf, vectorizer, text):
    # Tokenize paragraph into sentences
    sentences = sent_tokenize(text)
    
    # Initialize list to store predicted labels for each sentence
    sentence_predictions = []
    
    # Transform and predict sentiment for each sentence
    for sentence in sentences:
        sentence_transformed = vectorizer.transform([sentence])
        sentence_dense = sentence_transformed.toarray()
        prediction = clf.predict(sentence_dense)
        sentence_predictions.append(prediction)
    
    # Analyze sentiment distribution
    sentence_predictions_tuples = [tuple(pred) for pred in sentence_predictions]
    sentiment_counts = Counter(sentence_predictions_tuples)
    total_sentences = len(sentences)
    
    # Calculate percentage of each sentiment
    sentiment_percentages = {}
    for sentiment, count in sentiment_counts.items():
        percentage = (count / total_sentences) * 100
        sentiment_percentages[sentiment] = percentage
    
    # Determine the major sentiment
    major_sentiment = max(sentiment_counts, key=sentiment_counts.get)
    
    return {
        'sentence_details': list(zip(sentences, sentence_predictions)),
        'sentiment_percentages': sentiment_percentages,
        'major_sentiment': major_sentiment
    }