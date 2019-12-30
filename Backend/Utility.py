from bs4 import BeautifulSoup
from bs4.element import Comment
import re
import ftfy
from pprint import pprint
from cryptography.fernet import Fernet
# import requests


class Utility:

    def get_website_name_from_url(self, url):
        """
        Inputs: url (string)
        Outputs: nameOfTheWebpage (string)
            Fetches Websites name from the given url
            Takes url as a parameter
        """
        startingIndex = 0

        if(url.find('www.') >= 0):
            startingIndex = url.find('www.') + 4
        elif(url.find('//') >= 0):
            startingIndex = url.find('//') + 2
        elif(url.find('.') >= 0):
            startingIndex = url.find('.') + 1

        endingIndex = 0

        if(url.find('com') >= 0):
            endingIndex = url.find('.com')
        elif(url.find('io') >= 0):
            endingIndex = url.find('.io')
        elif(url.find('org') >= 0):
            endingIndex = url.find('.org')
        elif(url.find('ac.in') >= 0):
            endingIndex = url.find('.ac.in')
        filename = url[startingIndex: endingIndex]
        return filename

################## SHOULD BE IN ONE NODE #######################
    def tagVisible(self, element):  # , new_tags = []):
        """
            Checks if certain type of HTML tags/Comment/eliminates extra white spaces/new line character are in the text that's being parsed and filters them out.
            Default tag that we are checking for are listed below:
                ['style', 'script', 'head', 'title', 'meta', '[document]']

        """
        tagList = ['style', 'script', 'head', 'title', 'meta', '[document]']
        if element.parent.name in tagList:
            return False
        if isinstance(element, Comment):
            return False
        if re.match(r"[\r\n]+", str(element)):
            return False
        return True

    def textFromHtml(self, content):
        """ 
            Input : Response Object. (generic)
            Output: Fetches Text from the HTML and returns it. (string)

        """
        soup = BeautifulSoup(content.text, 'html.parser')
        texts = soup.findAll(text=True)
        # print(texts)
        # Filters the texts of all the unnecessary tags and
        visibleTexts = filter(self.tagVisible, texts)
        htmlText = ftfy.fix_text(u" ".join(t.strip() for t in visibleTexts))
        return htmlText

#################################################################

    def SentenceTokenizer(self, htmlText):
        """
            Inputs: htmlText (string)
            Outputs: List of Sentences (list)
        """
        sentences = re.split('(\.|!|\?)', htmlText)

        """ Prints Sentences in prettier way"""
        # for i, s in enumerate(sentences):
        #    print('-->Sentence %d: %s' % (i, s))

        return sentences

    def fetchQnAWithHtmlText(self, sentences):
        """
            Inputs : Sentences
            Outputs: dictOfQA
        """
        #sentences = self.SentenceTokenizer(var1)
        
        try:
            indexOfQuestions = []

            # Getting indexes of questions
            for i, sentence in enumerate(sentences):
                if(sentence == '?'):
                    indexOfQuestions.append(i-1)

            dictOfQA = {}

            for i in range(1, len(indexOfQuestions)):
                answer = ''
                for j in range(indexOfQuestions[i-1], indexOfQuestions[i]):
                    if(j not in indexOfQuestions):
                        answer += sentences[j]
                dictOfQA[sentences[indexOfQuestions[i-1]]] = answer

            """ 
                The above loop doesn't fetches the last question for obvious reasons.
            """
            lastanswer = ''
            for k in range(indexOfQuestions[len(indexOfQuestions)-1], len(sentences)):
                lastanswer += sentences[k]

            dictOfQA[sentences[indexOfQuestions[len(
                indexOfQuestions) - 1]]] = lastanswer
            
            return dictOfQA
        except:
            print(sentences)
            return {}

    # , indexOfQnAToFindHeirarchy=0):
    def fetchHtmlHierarchy(self, dictQnA, content):
        try:
            listOfQnA = []
            # pprint(dictQnA)
            for keys in dictQnA:
                listOfQnA.append(['credit', dictQnA[keys][2:], keys])
            listOfQnA.insert(0, ['Category', 'Answers', 'Questions'])

            # pprint(listOfQnA)
            # if(indexOfQnAToFindHeirarchy == 0):
            indexToSearchFor = int(len(listOfQnA) / 2)
            # else:
            # indexToSearchFor = indexOfQnAToFindHeirarchy

            textPatternQuestions = listOfQnA[indexToSearchFor][2].strip()[0:10]
            textPatternAnswers = listOfQnA[indexToSearchFor][1].strip()[0:10]
            soup = BeautifulSoup(content.text, 'html.parser')
            listOfQnAHeirarchies = []
            for textPattern in [textPatternQuestions, textPatternAnswers]:
                try:
                    textPatternTags = soup.body.findAll(
                        text=re.compile(textPattern))[0]
                    listOfTags = []
                    for parent in textPatternTags.parents:
                        listOfTags.append((parent.name, parent.attrs,))
                        if(parent.name == 'body'):
                            break
                    listOfQnAHeirarchies.append(listOfTags)
                except IndexError as e:
                    print("TEXT PATTERN \n \n \" " + textPattern +
                        "\" \n \n WASN'T FOUND IN THE HTML TEXT \n \n")
                    # print(e)
                    return []
            return listOfQnAHeirarchies
        except:
            print(content)
            print(dictQnA)
            return []

    def generateSelectorQuery(self,questionHierarchy,answerHierarchy):
        xPathListQuestion= []
        xPathListAnswer = []
        try:
            for tag in questionHierarchy:
                # print(tag)
                tagToAppend = ''
                if(tag[1]):
                    for key in tag[1]:
            #             print(tagToAppend)
                        try:
                            if(key == 'class' and tag[1][key] != []):
                                tagToAppend = tag[0] + '[class~=' + tag[1][key][0] + ']'
                                break
                            else:
                                tagToAppend = tag[0]
                        except IndexError as e:
                            print(e)
                else:
                    if(tag[0] not in ['p','strong','br','a','b','i','em','mark','sub','sup','small','del','ins','code','q','cite','blockquote']):
                        tagToAppend = tag[0]
                xPathListQuestion.append(tagToAppend)
            # print("XPATH QUESTION: ",xPathListQuestion)
        except IndexError as e:
            print(e)
        # print(xPathListQuestion)
        for tag in answerHierarchy:
            tagToAppend = ''
            # print(tag)
            if(tag[1]):
                try:    
                    for key in tag[1]:
                        if(key == 'class' and tag[1][key] != []):
                            tagToAppend = tag[0] + '[class~=' + tag[1][key][0] + ']'
                            break
                        else:
                            tagToAppend = tag[0]
                except IndexError as e:
                    print(e)
            else:
                if(tag[0] not in ['p','strong','br','a','b','i','em','mark','sub','sup','small','del','ins','code','q','cite','blockquote']):
                    tagToAppend = tag[0]
            xPathListAnswer.append(tagToAppend)
        # print("XPATH ANSWER: ",xPathListAnswer)

        if(len(xPathListQuestion) - len(xPathListAnswer) > 0):
            xPathListQuestion = xPathListQuestion[len(xPathListQuestion) - len(xPathListAnswer):]
        elif(len(xPathListQuestion) - len(xPathListAnswer) < 0):
            xPathListAnswer = xPathListAnswer[len(xPathListAnswer) - len(xPathListQuestion):]

        # print(len(xPathListQuestion) - len(xPathListAnswer))   
        selectorQueryQuestions = ' '.join(xPathListQuestion[::-1])#[len(xPathList) - 4:])
        selectorQueryAnswers = ' '.join(xPathListAnswer[::-1])#[len(xPathList) - 4:])
        
        # print(selectorQueryQuestions)
        # print(selectorQueryAnswers)#[:len(selectorQueryAnswers)-2])
        return [selectorQueryQuestions,selectorQueryAnswers]

    def encryptUrl(self,url):
        file = open('key.key', 'rb')
        key = file.read() # The key will be type bytes
        file.close()
        message = url.encode()
        f = Fernet(key)
        encrypted = f.encrypt(message)
        return encrypted

    def decryptUrl(self,url):
        file = open('key.key', 'rb')
        key = file.read() # The key will be type bytes
        file.close()
        encrypted = url
        f = Fernet(key)
        decrypted = f.decrypt(encrypted)
        return decrypted
