import spacy

# Carregar o modelo de idioma português
nlp = spacy.load("pt_core_news_sm")

# Exemplo de texto
texto = "Olá, como você está? Eu estou aprendendo processamento de linguagem natural."

# Processar o texto
doc = nlp(texto)

# Tokenização
tokens = [token.text for token in doc]
print("Tokens:", tokens)

# Remover stopwords
tokens_filtrados = [token.text for token in doc if not token.is_stop]
print("Tokens filtrados:", tokens_filtrados)

# Lematização
lematizados = [token.lemma_ for token in doc]
print("Lematizados:", lematizados)
