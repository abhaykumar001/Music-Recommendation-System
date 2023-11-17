import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
import pickle

df = pd.read_csv("spotify_millsongdata.csv")

# just some commands
# print(df.head(5))
# print(df.tail(3))

ds=df.sample(5000).drop('link', axis=1).reset_index(drop=True)
# ds=ds.sample(6000)

# to see the total sample space which we are using
# print(ds.shape)

# TEXT CLEANING
ds['text']=ds['text'].str.lower().replace(r'^\w\s','').replace(r'\n',' ' , regex=True)
# print(ds.head(10))

# TOKENIZATION,STEAMING,VECTORISATION
# TOKENIZATION STARTS
stemmer=PorterStemmer()
def token(txt):
    token=nltk.word_tokenize(txt)
    a=[stemmer.stem(w) for w in token]
    # to print the tokenized word from the string
    # print(" ".join(a))
    return " ".join(a)

# checking the function (working or not)
token("you are beautiful,beauty,beauty ful")
ds['text']=ds['text'].apply(lambda q : token(q))
#  TOKENIZATION ENDS

#  VECTORIZATION STARTS
tfidf_vectorizer = TfidfVectorizer(analyzer='word', stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(ds['text'])
cosine_sim = cosine_similarity(tfidf_matrix)



# ds[ds['song'] == 'All The Right Moves']
# result = ds[ds['song'] == 'All The Right Moves'].index[0]

# def recommender(song_name):
#     idx = ds[ds['song'] == song_name].index[0]
#     distance=sorted(list(enumerate(cosine_sim[idx])),reverse=True,key=lambda x:x[1])
#     song=[]
#     for s_id in distance[1:5]:
#         song.append(ds.iloc[s_id[0]].song)
#     return song
#
# recommender('you are happy')
def recommender(song_name):
    # Find the index of the song_name in the DataFrame
    idx = ds['song'].eq(song_name).idxmax()
    # Calculate cosine similarity
    similarity_scores = list(enumerate(cosine_sim[idx]))
    # Sort by similarity in descending order
    sorted_scores = sorted(similarity_scores, reverse=True, key=lambda x: x[1])
    # Get the top 4 similar songs (excluding the input song itself)
    similar_songs = [ds.iloc[s_id[0]].song for s_id in sorted_scores[1:11]]
    print(similar_songs)
    return 

# checking the function
# recommender('sad song')
pickle.dump(cosine_sim,open("similarity","wb"))
pickle.dump(ds,open("ds","wb"))





