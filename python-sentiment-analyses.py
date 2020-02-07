
from textblob import TextBlob



testimonial = TextBlob("Textblob is amazingly simple to use. What a great fun!")  # Sentiment(polarity=0.39166666666666666, subjectivity=0.4357142857142857)
testimonial = TextBlob("Textblob is trashy. What a great deception!")  # Sentiment(polarity=1.0, subjectivity=0.75)
testimonial = TextBlob("Textblob is bad. What a great deception!")  # Sentiment(polarity=0.15000000000000008, subjectivity=0.7083333333333333)
testimonial = TextBlob("Textblob is bad. What a deception!")  # Sentiment(polarity=-0.8749999999999998, subjectivity=0.6666666666666666)
testimonial = TextBlob("Textblob sucks.")  # Sentiment(polarity=-0.3, subjectivity=0.3)

print('testimonial:               ' + str(testimonial))
print('testimonial sentiment:     ' + str(testimonial.sentiment))
print('testimonial polarity:      ' + str(testimonial.sentiment.polarity))
print('testimonial subjectivity:  ' + str(testimonial.sentiment.subjectivity))