from flask import Flask, render_template, request
import os
import docx2txt
import PyPDF2
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from collections import Counter
import re

app = Flask(_name_)

# Fungsi untuk melakukan preprocessing teks (case folding, tokenisasi, filtering, stemming)
def preprocess_text(text):
    # Case folding
    text = text.lower()

    # Tokenisasi (diasumsikan pemisah kata adalah spasi)
    tokens = text.split()

    # Filter karakter non-from flask import Flask, render_template, request
import os
import docx2txt
import PyPDF2
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from collections import Counter
import re

app = Flask(_name_)

# Fungsi untuk melakukan preprocessing teks (case folding, tokenisasi, filtering, stemming)
def preprocess_text(text):
    # Case folding
    text = text.lower()

    # Tokenisasi (diasumsikan pemisah kata adalah spasi)
    tokens = text.split()

    # Filter karakter non-alfanumerik (misalnya: tanda baca)
    tokens = [word.strip(".,?!-;:\"'()[]{}") for word in tokens]

    # Stemming menggunakan Sastrawi
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    return stemmed_tokens

# Fungsi untuk pencarian menggunakan sequential search
def sequential_search(keyword, tokens):
    found = []
    for index, token in enumerate(tokens):
        if keyword in token:
            found.append((index, token))
    return found

# Fungsi untuk melakukan stemming pada query
def stem_query(query):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    return stemmer.stem(query)

@app.route('/')
def index():
    folder_path = 'files'  # Ubah dengan path folder dokumen
    files_list = os.listdir(folder_path)
    return render_template('index.html', files_list=files_list)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    tokens_query = preprocess_text(query)  # Melakukan tokenisasi kalimat

    stemmed_query = [stem_query(token) for token in tokens_query]  # Melakukan stemming pada setiap kata dalam kalimat

    folder_path = 'files'  # Ubah dengan path folder dokumen

    # Lakukan pencarian di setiap file dalam folder
    search_results = []
    similarity_scores = {}  # Simpan skor kesamaan kata dengan query untuk setiap file
    word_count = {}  # Simpan jumlah kata untuk setiap file
    word_freq = {}  # Simpan frekuensi kemunculan kata untuk setiap file

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if file_name.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                tokens = preprocess_text(text)
                found = [token for token in tokens if token in stemmed_query]  # Cek setiap kata dalam kalimat pada teks
                if found:
                    search_results.append(file_name)
                    similarity_scores[file_name] = len(found) / len(tokens)
                    word_count[file_name] = len(tokens)
                    word_freq[file_name] = Counter(tokens)
        elif file_name.endswith('.docx'):
            text = docx2txt.process(file_path)
            tokens = preprocess_text(text)
            found = [token for token in tokens if token in stemmed_query]
            if found:
                search_results.append(file_name)
                similarity_scores[file_name] = len(found) / len(tokens)
                word_count[file_name] = len(tokens)
                word_freq[file_name] = Counter(tokens)
        elif file_name.endswith('.pdf'):
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ''
                num_pages = len(pdf_reader.pages)
                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()
                tokens = preprocess_text(text)
                found = [token for token in tokens if token in stemmed_query]
                if found:
                    search_results.append(file_name)
                    similarity_scores[file_name] = len(found) / len(tokens)
                    word_count[file_name] = len(tokens)
                    word_freq[file_name] = Counter(tokens)

    # Sort hasil berdasarkan skor kesamaan (paling mirip ke paling tidak mirip)
    sorted_results = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)
    

    # Tampilkan hasil pencarian, kesamaan kata dengan query, jumlah kata, dan kemunculan kata
    return render_template('index.html', search_results=search_results, similarity_scores=sorted_results, stemmed_query=stemmed_query, word_count=word_count, word_freq=word_freq)

if _name_ == '_main_':
    app.run(debug=True)alfanumerik (misalnya: tanda baca)
    tokens = [word.strip(".,?!-;:\"'()[]{}") for word in tokens]

    # Stemming menggunakan Sastrawi
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    return stemmed_tokens

# Fungsi untuk pencarian menggunakan sequential search
def sequential_search(keyword, tokens):
    found = []
    for index, token in enumerate(tokens):
        if keyword in token:
            found.append((index, token))
    return found

# Fungsi untuk melakukan stemming pada query
def stem_query(query):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    return stemmer.stem(query)

@app.route('/')
def index():
    return render_template('cb.html')

@app.route('/search', methods=['POST'])
def search():
    folder_path = 'files'  # Ubah dengan path folder dokumen
    files_list = os.listdir(folder_path)
    query = request.form['query']
    tokens_query = preprocess_text(query)  # Melakukan tokenisasi kalimat

    stemmed_query = [stem_query(token) for token in tokens_query]  # Melakukan stemming pada setiap kata dalam kalimat

    folder_path = 'files'  # Ubah dengan path folder dokumen

    # Lakukan pencarian di setiap file dalam folder
    search_results = []
    similarity_scores = {}  # Simpan skor kesamaan kata dengan query untuk setiap file
    word_count = {}  # Simpan jumlah kata untuk setiap file
    word_freq = {}  # Simpan frekuensi kemunculan kata untuk setiap file

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if file_name.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                tokens = preprocess_text(text)
                found = [token for token in tokens if token in stemmed_query]  # Cek setiap kata dalam kalimat pada teks
                if found:
                    search_results.append(file_name)
                    similarity_scores[file_name] = len(found) / len(tokens)
                    word_count[file_name] = len(tokens)
                    word_freq[file_name] = Counter(tokens)
        elif file_name.endswith('.docx'):
            text = docx2txt.process(file_path)
            tokens = preprocess_text(text)
            found = [token for token in tokens if token in stemmed_query]
            if found:
                search_results.append(file_name)
                similarity_scores[file_name] = len(found) / len(tokens)
                word_count[file_name] = len(tokens)
                word_freq[file_name] = Counter(tokens)
        elif file_name.endswith('.pdf'):
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ''
                num_pages = len(pdf_reader.pages)
                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()
                tokens = preprocess_text(text)
                found = [token for token in tokens if token in stemmed_query]
                if found:
                    search_results.append(file_name)
                    similarity_scores[file_name] = len(found) / len(tokens)
                    word_count[file_name] = len(tokens)
                    word_freq[file_name] = Counter(tokens)

    # Sort hasil berdasarkan skor kesamaan (paling mirip ke paling tidak mirip)
    sorted_results = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)
    

    # Tampilkan hasil pencarian, kesamaan kata dengan query, jumlah kata, dan kemunculan kata
    return render_template('index.html', search_results=search_results, similarity_scores=sorted_results, stemmed_query=stemmed_query, word_count=word_count, word_freq=word_freq, files_list=files_list)

if _name_ == '_main_':
    app.run(debug=True)