import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

# Baixar recursos necessários
nltk.download('punkt')
nltk.download('stopwords')

# Exemplo de texto
texto = "Olá, como você está? Eu estou aprendendo processamento de linguagem natural."

# Tokenização
tokens = word_tokenize(texto, language='portuguese')
print("Tokens:", tokens)

# Remover stopwords
stop_words = set(stopwords.words('portuguese'))
tokens_filtrados = [word for word in tokens if word.lower() not in stop_words]
print("Tokens filtrados:", tokens_filtrados)

# Stemização (reduzir palavras à sua raiz)
stemmer = RSLPStemmer()
raizes = [stemmer.stem(word) for word in tokens_filtrados]
print("Raízes:", raizes)
