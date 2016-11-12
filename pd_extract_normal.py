#!/home/morgan/anaconda2/bin/python
import nltk, re, pprint
import os
import docx2txt
import regex
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist

docx_file = "/home/morgan/Desktop/pd/schizoid_docx/4.docx"

#open corpus file, output as token file
with open(docx_file) as in_file, open("/home/morgan/Desktop/pd/schizoid_tokens/tokens_schizoid_normal4.txt", "w") as out_file:
	#allows docx file to be processed by python
	text = docx2txt.process(docx_file)
	#removes non-words from docx file
	clean_text = re.sub("[^a-z-0-9]"," ", text)
	#declares english stop words to be removed later
	stop_words = set(stopwords.words("english"))
	#tokenizes cleaned text file
	word_tokens = word_tokenize(clean_text)
	#runs frequency distribution on the 100 most common words
	fdist1 = FreqDist(word_tokens)
	print fdist1.most_common(100)
	filtered_sentence = [w for w in word_tokens if not w in stop_words]
	filtered_sentence = []
	for w in word_tokens:
		if w not in stop_words:
			filtered_sentence.append(w)
			for item in word_tokens:
				#print item
				out_file.write("%s\n" % item)