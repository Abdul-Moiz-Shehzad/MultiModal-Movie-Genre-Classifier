from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import re
stop_words=stopwords.words('english')
def preprocess_text(text: str,return_lst=True) -> list:
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    text=text.lower()
    tokens=word_tokenize(text)
    lst=[]
    for token in tokens:
        if token not in stop_words:
            token=WNL.lemmatize(token)
            lst.append(token)
    if return_lst:
        return lst
    else:
        return ' '.join(lst)