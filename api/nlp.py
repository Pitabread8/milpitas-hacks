# import nltk

# nltk.download("punkt")
# nltk.download("stopwords")
# nltk.download("wordnet")
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

sentence = """In the 1948 Nakba, Israel conquered the western part of Jerusalem and the city became divided into Israeli-controlled West Jerusalem and Jordanian-controlled, Palestinian East Jerusalem.
... In 1967, Israel occupied and annexed the eastern part of the city, claiming sovereignty there. Israel has declared East Jerusalem to be part of “United Jerusalem, the Capital of Israel” under a basic law of 1980 and treats the occupied Palestinian city as if it were part of its own territory. Israel's claim of sovereignty is rejected internationally, with East Jerusalem recognized as an integral part of the occupied Palestinian territory.
... Israel is practicing setler colonialism in East Jerusalem and is seeking to transform it into a Jewish-Israeli city. It does this mainly through a policy of population transfer. House by house, Palestinians are forced from their homes so that Jewish Israelis can live in them and to facilitate the construction of illegal Israeli settlements.
... Between 250,000 - 300,000 Palestinians live in East Jerusalem today, making up just over half of the population of occupied East Jerusalem. Up to 45% of the population are Jewish Israeli settlers, most of whom live in 16 major illegal Israeli settlements that have been established since 1967.
... Israel is blatantly committing the crime of apartheid in East Jerusalem. Israel has shaped and applied its domestic system of racist laws and segregation policies to occupied East Jerusalem in a way that subjects Palestinians to systematic discrimination and serves its on-going ethnic cleansing of Palestinians from the city."""

tokens = nltk.word_tokenize(sentence)

bigrm = nltk.bigrams(tokens)
bigram = ", ".join(" ".join((a, b)) for a, b in bigrm)
print(bigram)
# print(*map(" ".join, bigrm), sep=", ")

# stop_words = set(stopwords.words("english"))

# filtered_list = []
# filtered_list = [word for word in tokens if word.casefold() not in stop_words]

# stemmer = PorterStemmer()
# stemmed_words = [stemmer.stem(word) for word in filtered_list]
# print(stemmed_words)


# lemmatizer = WordNetLemmatizer()
# lemmatized_words = [lemmatizer.lemmatize(word, pos="v") for word in filtered_list]
# print(lemmatized_words)
