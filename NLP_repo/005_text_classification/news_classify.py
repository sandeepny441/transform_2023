import re
import nltk

from sklearn.datasets import fetch_20newsgroups

from nltk.stem import WordNetLemmatize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import TweetTokenizer
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer

# Load the 20 Newsgroups dataset
newsgroups = fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'))

# Initialize the lemmatizer and the list of stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


# Download NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Define a function to preprocess the text
def preprocess_text(text, remove_urls=False, 
                    remove_emails=False, 
                    spell_correct=False, 
                    lemmatize=True, 
                    stemmer='wordnet', 
                    chunking=False, 
                    remove_punct=False):
    # Remove URLs and email addresses if specified
    if remove_urls: 
        text = re.sub(r'http\S+|www.\S+', '', text)
    if remove_emails: 
        text = re.sub(r'\S+@\S+', '', text)
    
    # Remove special characters and digits
    text = re.sub(r'\W|\d', ' ', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Tokenize the text
    tokenizer = TweetTokenizer() # Using tweet tokenizer as it is best suited for social media text
    tokens = tokenizer.tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Spell correction if specified
    if spell_correct:
        tokens = [spell.correction(token) for token in tokens]
    
    # Lemmatization if specified
    if lemmatize:
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Stemming if specified
    if stemmer == 'porter':
        stemmer = PorterStemmer()
    elif stemmer == 'lancaster':
        stemmer = LancasterStemmer()
    elif stemmer == 'snowball':
        stemmer = SnowballStemmer("english")
    else:
        stemmer = wordnet.WordNetLemmatizer()
    tokens = [stemmer.stem(token) for token in tokens]
    
    # Chunking if specified
    if chunking:
        grammar = "NP: {<DT>?<JJ>*<NN>}"
        cp = nltk.RegexpParser(grammar)
        tagged = nltk.pos_tag(tokens)
        tree = cp.parse(tagged)
        for subtree in tree.subtrees():
            if subtree.label() == 'NP':
                tokens.append(' '.join([word for word, pos in subtree.leaves()]))
    
    # Remove punctuation if specified
    if remove_punct:
        tokens = [token for token in tokens if token.isalpha()]
    
    # Join tokens back into a single string
    text = ' '.join(tokens)
    
    return text



# Apply preprocessing to the dataset
processed_data = [preprocess_text(text) for text in newsgroups.data]

# Print the first 5 processed texts

print(processed_data[:5])
