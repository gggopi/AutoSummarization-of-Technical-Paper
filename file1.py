# coding=UTF-8
from __future__ import division
import re

# This is a naive text summarization algorithm
# Created by Shlomi Babluki
# April, 2013
 
 
class SummaryTool(object):
 
    # Naive method for splitting a text into sentences
    def split_content_to_sentences(self, content):
		content = content.replace("\n", ". ")
		return content.split(". ")
 
    # Naive method for splitting a text into paragraphs
    def split_content_to_paragraphs(self, content):
        return content.split("\n\n")
 
    # Caculate the intersection between 2 sentences
    def sentences_intersection(self, sent1, sent2):
 
        # split the sentence into words/tokens
        s1 = set(sent1.split(" "))
        s2 = set(sent2.split(" "))
 
        # If there is not intersection, just return 0
        if (len(s1) + len(s2)) == 0:
            return 0
 
        # We normalize the result by the average number of words
        return len(s1.intersection(s2)) / ((len(s1) + len(s2)) / 2)
 
    # Format a sentence - remove all non-alphbetic chars from the sentence
    # We'll use the formatted sentence as a key in our sentences dictionary
    def format_sentence(self, sentence):
        sentence = re.sub(r'\W+', '', sentence)
        return sentence
 
    # Convert the content into a dictionary <K, V>
    # k = The formatted sentence
    # V = The rank of the sentence
    def get_senteces_ranks(self, content):
 
        # Split the content into sentences
        sentences = self.split_content_to_sentences(content)
 
        # Calculate the intersection of every two sentences
        n = len(sentences)
        values = [[0 for x in xrange(n)] for x in xrange(n)]
        for i in range(0, n):
            for j in range(0, n):
                values[i][j] = self.sentences_intersection(sentences[i], sentences[j])
 
        # Build the sentences dictionary
        # The score of a sentences is the sum of all its intersection
        sentences_dic = {}
        for i in range(0, n):
            score = 0
            for j in range(0, n):
                if i == j:
                    continue
                score += values[i][j]
            sentences_dic[self.format_sentence(sentences[i])] = score
        return sentences_dic
 
    # Return the best sentence in a paragraph
    def get_best_sentence(self, paragraph, sentences_dic):
 
        # Split the paragraph into sentences
        sentences = self.split_content_to_sentences(paragraph)
 
        # Ignore short paragraphs
        if len(sentences) < 2:
            return ""
 
        # Get the best sentence according to the sentences dictionary
        best_sentence = ""
        max_value = 0
        for s in sentences:
            strip_s = self.format_sentence(s)
            if strip_s:
                if sentences_dic[strip_s] > max_value:
                    max_value = sentences_dic[strip_s]
                    best_sentence = s
 
        return best_sentence
 
    # Build the summary
    def get_summary(self, title, content, sentences_dic):
 
        # Split the content into paragraphs
        paragraphs = self.split_content_to_paragraphs(content)
 
        # Add the title
        summary = []
        summary.append(title.strip())
        summary.append("")
 
        # Add the best sentence from each paragraph
        for p in paragraphs:
            sentence = self.get_best_sentence(p, sentences_dic).strip()
            if sentence:
                summary.append(sentence)
 
        return ("\n").join(summary)
 
 
# Main method, just run "python summary_tool.py"
def main():



	opt = open('output1.txt','w')
	opt1 = open('output1.txt','a')

	# Demo
	
	# infile = open('int1')
	# outfile = open('int2', 'w')

	# replacements = {'<':'\n<', '>':'>\n'}

	# for line in infile:
		# for src, target in replacements.iteritems():
			# line = line.replace(src, target)
		# outfile.write(line)
	# infile.close()
	# outfile.close()
	import re
	# with open('negro.html') as infile, open('int1', 'w') as outfile:
		# copy = False
		# str=""
		# p=re.compile('.*<body.*',re.IGNORECASE)
		# p1=re.compile('.*</body>.*',re.IGNORECASE)
		# for line in infile:
			# if p.match(line.strip()):#line.strip() == "<body>":
				# copy = True
				# str=""	
			# elif p1.match(line.strip()):# == "</body>":
				# copy = False
				# #count = count + 1
				# print str
				# #star.append(str)
				
			# elif copy:
				# str= str + line
				# print str
				# outfile.write(line)

				
	# infile = open('int1')
	# outfile = open('int2', 'w')

	# replacements = {'\n\n':'#~$','\n':' ','<':'\n<', '>':'>\n','<br>':'','<hr>':'','<br/>':''}

	# for line in infile:
		# for src, target in replacements.iteritems():
			# line = line.replace(src, target)
		# line = re.sub('<.*>\n',' ',line,re.IGNORECASE)
		# line = re.sub('</.*>\n',' ',line,re.IGNORECASE)
		# outfile.write(line)
	# infile.close()
	# outfile.close()

	with open('n1.html') as infile, open('int1', 'w') as outfile:
		copy = False
		str=""
		p=re.compile('.*<body.*',re.IGNORECASE)
		p1=re.compile('.*<h[1-9]>.*references.*</h[1-9]>',re.IGNORECASE)
		for line in infile:
			if p.match(line.strip()):#line.strip() == "<body>":
				copy = True
				str=""	
			elif p1.match(line.strip()):# == "</body>":
				copy = False
				#count = count + 1
				print str
				#star.append(str)
				
			elif copy:
				str= str + line
				#print str
				outfile.write(line)
		
					
	infile = open('int1')
	outfile = open('int2', 'w')

	replacements = {'\n':' ','<':'\n<', '>':'>\n'}#'<br>':'','<hr>':'','<br/>':''}
		#line = re.sub('<.*>\n',' ',line,re.IGNORECASE)
		#line = re.sub('</.*>\n',' ',line,re.IGNORECASE)
	#for line in infile:
	for line in infile:
		
		for src, target in replacements.iteritems():
			line = line.replace(src, target)
		line = re.sub('\[.*\]','',line,re.IGNORECASE)
		#line = re.sub('<H.*>','$%^',line,re.IGNORECASE)
		#line = re.sub('</H.*>','@#$',line,re.IGNORECASE
		line = re.sub('<p.*>','$%^',line,re.IGNORECASE)
		line = re.sub('</p.*>','@#$',line,re.IGNORECASE)
		line = re.sub('<.*>','',line,re.IGNORECASE)
		line = re.sub('</.*>','',line,re.IGNORECASE)
		#line = line.replace('$%^','\n<h>')
		#line = line.replace('@#$','</h>')
		#line = re.sub('{\n}*','\n',line,re.IGNORECASE)
		#line = re.sub('\.   ','.\n<h>\n\n</h>\n',line,re.IGNORECASE)
		
		outfile.write(line)
	infile.close()
	outfile.close()
	
	#from array import *
	#strarr=array()
	with open('int2') as infile, open('int3', 'w') as outfile:
		copy = False
		star=[]
		str=""
		count = 0
		for line in infile:
			if line.strip() == "$%^":
				copy = True
				str=""	
			elif line.strip() == "@#$":
				copy = False
				count = count + 1
				#str= str + '.'
				print str
				#opt1.write(str)
				#opt1.write("\nding\n")
				star.append(str)
				
			elif copy:
				str= str + line
				
				outfile.write(line)
		print star
		
	for x in star:
		if len(x)>130:
			title = " "

			content = x 
			# Create a SummaryTool object
			st = SummaryTool()

			# Build the sentences dictionary
			sentences_dic = st.get_senteces_ranks(content)

			# Build the summary with the sentences dictionary
			summary = st.get_summary(title, content, sentences_dic)

			# Print the summary
			print summary
			opt1.write(summary+'.')
			#opt.close()
			# Print the ratio between the summary length and the original length
			print ""
			
			#opt1.write("\n")
			print "Original Length %s" % (len(title) + len(content))
			#opt1.write("Original Length %s" % (len(title) + len(content)) + '\n')
			print "Summary Length %s" % len(summary)
			#opt1.write("Summary Length %s" % len(summary) + "\n")
			print "Summary Ratio: %s" % (100 - (100 * (len(summary) / (len(title) + len(content)))))
			#opt1.write("Summary Ratio: %s" % (100 - (100 * (len(summary) / (len(title) + len(content))))) + '\n')

	 
if __name__ == '__main__':
    main()