import string
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags

"""This function will capitalize the first letter of the first word in every sentence"""
def sentence_capitalizer(text):
	# tokenize the text by sentences
	final_Sentences = []
	sentences = nltk.sent_tokenize(text)
	print (sentences)
	# for each sentence in the text, capitalize the first word
	for i in range(0, len(sentences)):
		temp = sentences[i].title()
		
		final_Sentences.append(noun_capitalizer(temp))
		#sentences[i] = sentences[i].strip().capitalize()
	return " ".join(final_Sentences)

"""This function will capitalize the proper nouns"""
def noun_capitalizer(sentence):

	#Blank Sentence
	sentences_new = ''

	# Find the NER Tags
	ne_tree = ne_chunk(pos_tag(word_tokenize(sentence)))
	tagging = tree2conlltags(ne_tree)
	
	print (tagging)
	
	for i in range(0,len(tagging)):
		flag = 0

		if tagging[i][1] == 'NN' or tagging[i][1] == 'NNS'or tagging[i][1] == 'NNP' or tagging[i][1] == 'NNPS':
			if tagging[i][2].find('PERSON') >= 0 :
				flag = flag  + 1
			elif tagging[i][2].find('GPE') >=0:
				flag = flag  + 1
			elif tagging[i][2].find('ORGANIZATION') >=0:
				if (i-1) < len(tagging) and not(tagging[i-1][2].find('ORGANIZATION') >=0 or tagging[i-1][0] == '.' or tagging[i-1][0] == ';' or tagging[i-1][0] == ','):
					flag = flag  + 1
			
		elif tagging[i][1] == 'PRP' and tagging[i][0] == 'I':	
			flag = flag  + 1
		elif tagging[i][0] in string.punctuation:
			flag = flag  + 1
		elif i == 0:
			flag =flag  + 1
		elif (i-1) < len(tagging):
			if tagging[i-1][0] == '.':
				flag = flag + 1

		if(i == len(tagging) - 2):
			if flag > 0:
				sentences_new = sentences_new +tagging[i][0]
			else:
				s= tagging[i][0]
				sentences_new = sentences_new +s[0].lower() + s[1:] 
		elif (i+1) < len(tagging) and (tagging[i+1][0] == ',' or tagging[i+1][0] == '.' or tagging[i+1][0] == ';' ):
			if flag > 0:
				sentences_new = sentences_new + tagging[i][0]
			else:
				s= tagging[i][0]
				sentences_new = sentences_new + s[0].lower() + s[1:]
		else:
			if flag > 0:
				sentences_new = sentences_new + tagging[i][0] + ' '
			else:
				s= tagging[i][0]
				sentences_new = sentences_new + s[0].lower() + s[1:]  + ' '

	return (sentences_new[:-1])

"""This function will be the main function of the program"""
def main_function():

	#Input File read and remove white spaces from both sides
	input_file = open("test.txt", 'r')
	input_text = input_file.read()

	#Input text is :
	print("Input Text is: " + input_text)


    #Convert it to lower case
	input_text = input_text.lower()


	#Convert first character of each sentence to upper case
	output_text = sentence_capitalizer(input_text)
	print("Output Text = " + output_text)
	input_file.close()

# run the main function
if __name__ == '__main__':
    main_function()


	

