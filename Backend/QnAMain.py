from Utility import *
import requests
from pprint import pprint
import csv
import os
from firebaseUtil import *


# url = "https://experience.imiconnect.io/faqs"
# url = "https://www.icicibank.com/nri-banking/faq/investment/portfolio-investment-scheme-faqs.page?"
# url = "https://unity3d.com/unity/faq"
# url = "https://www.textlocal.in/mobile-marketing-guides/faq#Troubleshooting"
# url = "https://www.textlocal.com/support/faq/"
# url = "https://hpromise.hyundai.co.in/footer/faq#/C15"
# url = "https://www.swiggyassist.in/faq"
# url = "https://www.centrica.com/careers/application-faqs"
# url = "https://customerservices.npower.com/app/answers/list/st/5/page/1"
# url = "https://www.hdfcbank.com/personal/faq/faq-inner/gts8mint-gts8miol"
url = "https://www.banking.barclaysus.com/faq.html"


def getQuenstionsFromQuery(questionSelectorQuery, htmlContent):
    access_token = {'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjVkNjhkMmM2OTQzM2MwMDAxMjg1NzJlMiIsInJvbGUiOiJmbG93In0.5rX3TBpcf7i00KTWkywOsW-dRilkmnBLl5NIheklAos'}  # 'x-access-token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik16RTRNekF3TlRJM05UQTBOVVpETURnd01qSkdOVEJCTnpKQ056ZzVSa0V5TTBWQk5UTTRNdyJ9.eyJuaWNrbmFtZSI6ImRpbGlwLnAiLCJuYW1lIjoiZGlsaXAucEBpbWltb2JpbGUuY29tIiwicGljdHVyZSI6Imh0dHBzOi8vcy5ncmF2YXRhci5jb20vYXZhdGFyLzgyODEzMTM5OWI3YmVhNDBhNjVhMmI5OTRmMTQwOTgwP3M9NDgwJnI9cGcmZD1odHRwcyUzQSUyRiUyRmNkbi5hdXRoMC5jb20lMkZhdmF0YXJzJTJGZGkucG5nIiwidXBkYXRlZF9hdCI6IjIwMTktMDgtMjhUMDU6NTE6NTUuNzIyWiIsImVtYWlsIjoiZGlsaXAucEBpbWltb2JpbGUuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vZGV2LXowcTB6bjZsLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZDBjYTQ2YzdhMGJlYTBkMGM3MDg1NDAiLCJhdWQiOiJQS3JERUJZOUhxTEcxSHZSSWdOMGp6S0RfT2lLd0NRbCIsImlhdCI6MTU2Njk3MTkzMywiZXhwIjoxNTY3MDA3OTMzLCJhdF9oYXNoIjoic3dRMTdCeW9rTDNYMV9uTWtha2ZmZyIsIm5vbmNlIjoienZicEJWUHBYUHoycmE5aEMwYjBSeDRFZVJjbzVzbzkifQ.E_wL6zKWzqwHun0nszKsdiddt1fZVxeI6JPY2vrhPmf-j7nQVytuLBliWuZTSjX_X9I2sZTQJ-NoEWu6P7vXjcJky2mbYX31AU0aU0MQ4kFM9Kb2h6VZtnE-7Fv9WipuEz4BJZ1gbo5LU4jku0ZFvIVEwfMFKJ9kdDQjlvPd5zIxqEM2wAz0_w_msTnIxc_LPBw0BQ0iAKNZxBMjgmX6cqObuX5zvPiml7tkUd-oQKktE1rs4doMBacKVHwLbj4EBANCMgBAwL_-cCCXtOszVreoXFo_kcfjVBFMnIQN5q5jxerRE86VNwPazTjoDzj860ulGIg9vFxeBdJn74JKwA'}
    questionData = {'query_selector': questionSelectorQuery,
                    'html': str(htmlContent)}
    listOfQuestions = []
    try:
        questionsResponse = requests.post(
            'https://172.16.250.234:7070/api/v1/cheerio', headers=access_token, json=questionData)
        try:
            print(questionsResponse.json())
            listOfQuestions = questionsResponse.json()['data']
        except KeyError as e:
            print("No Output recieved")
            print(e)
            print(questionsResponse.json())
    except:
        print(" Bad Response")
    return listOfQuestions


def getAnswersFromQuery(answerSelectorQuery, htmlContent):
    access_token = {'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjVkNjhkMmM2OTQzM2MwMDAxMjg1NzJlMiIsInJvbGUiOiJmbG93In0.5rX3TBpcf7i00KTWkywOsW-dRilkmnBLl5NIheklAos'}  # 'x-access-token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik16RTRNekF3TlRJM05UQTBOVVpETURnd01qSkdOVEJCTnpKQ056ZzVSa0V5TTBWQk5UTTRNdyJ9.eyJuaWNrbmFtZSI6ImRpbGlwLnAiLCJuYW1lIjoiZGlsaXAucEBpbWltb2JpbGUuY29tIiwicGljdHVyZSI6Imh0dHBzOi8vcy5ncmF2YXRhci5jb20vYXZhdGFyLzgyODEzMTM5OWI3YmVhNDBhNjVhMmI5OTRmMTQwOTgwP3M9NDgwJnI9cGcmZD1odHRwcyUzQSUyRiUyRmNkbi5hdXRoMC5jb20lMkZhdmF0YXJzJTJGZGkucG5nIiwidXBkYXRlZF9hdCI6IjIwMTktMDgtMjhUMDU6NTE6NTUuNzIyWiIsImVtYWlsIjoiZGlsaXAucEBpbWltb2JpbGUuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vZGV2LXowcTB6bjZsLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZDBjYTQ2YzdhMGJlYTBkMGM3MDg1NDAiLCJhdWQiOiJQS3JERUJZOUhxTEcxSHZSSWdOMGp6S0RfT2lLd0NRbCIsImlhdCI6MTU2Njk3MTkzMywiZXhwIjoxNTY3MDA3OTMzLCJhdF9oYXNoIjoic3dRMTdCeW9rTDNYMV9uTWtha2ZmZyIsIm5vbmNlIjoienZicEJWUHBYUHoycmE5aEMwYjBSeDRFZVJjbzVzbzkifQ.E_wL6zKWzqwHun0nszKsdiddt1fZVxeI6JPY2vrhPmf-j7nQVytuLBliWuZTSjX_X9I2sZTQJ-NoEWu6P7vXjcJky2mbYX31AU0aU0MQ4kFM9Kb2h6VZtnE-7Fv9WipuEz4BJZ1gbo5LU4jku0ZFvIVEwfMFKJ9kdDQjlvPd5zIxqEM2wAz0_w_msTnIxc_LPBw0BQ0iAKNZxBMjgmX6cqObuX5zvPiml7tkUd-oQKktE1rs4doMBacKVHwLbj4EBANCMgBAwL_-cCCXtOszVreoXFo_kcfjVBFMnIQN5q5jxerRE86VNwPazTjoDzj860ulGIg9vFxeBdJn74JKwA'}
    answerData = {'query_selector': answerSelectorQuery,
                  'html': str(htmlContent)}
    listOfAnswers = []
    try:
        answersResponse = requests.post(
            'https://172.16.250.234:7070/api/v1/cheerio', headers=access_token, json=answerData)
        try:
            print(answersResponse)
            listOfAnswers = answersResponse.json()['data']
            for i, answer in enumerate(listOfAnswers):
                if("?" in answer):
                    listOfAnswers[i] = re.split('(\?)', answer)[2]
        except KeyError as e:
            print("No Output recieved")
            print(answersResponse.json())
    except:
        print("Bad Response")
    return listOfAnswers


def getCategoryFromQuery(categorySelectorQuery, htmlContent):
    access_token = {'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjVkNjhkMmM2OTQzM2MwMDAxMjg1NzJlMiIsInJvbGUiOiJmbG93In0.5rX3TBpcf7i00KTWkywOsW-dRilkmnBLl5NIheklAos'}  # 'x-access-token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik16RTRNekF3TlRJM05UQTBOVVpETURnd01qSkdOVEJCTnpKQ056ZzVSa0V5TTBWQk5UTTRNdyJ9.eyJuaWNrbmFtZSI6ImRpbGlwLnAiLCJuYW1lIjoiZGlsaXAucEBpbWltb2JpbGUuY29tIiwicGljdHVyZSI6Imh0dHBzOi8vcy5ncmF2YXRhci5jb20vYXZhdGFyLzgyODEzMTM5OWI3YmVhNDBhNjVhMmI5OTRmMTQwOTgwP3M9NDgwJnI9cGcmZD1odHRwcyUzQSUyRiUyRmNkbi5hdXRoMC5jb20lMkZhdmF0YXJzJTJGZGkucG5nIiwidXBkYXRlZF9hdCI6IjIwMTktMDgtMjhUMDU6NTE6NTUuNzIyWiIsImVtYWlsIjoiZGlsaXAucEBpbWltb2JpbGUuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vZGV2LXowcTB6bjZsLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZDBjYTQ2YzdhMGJlYTBkMGM3MDg1NDAiLCJhdWQiOiJQS3JERUJZOUhxTEcxSHZSSWdOMGp6S0RfT2lLd0NRbCIsImlhdCI6MTU2Njk3MTkzMywiZXhwIjoxNTY3MDA3OTMzLCJhdF9oYXNoIjoic3dRMTdCeW9rTDNYMV9uTWtha2ZmZyIsIm5vbmNlIjoienZicEJWUHBYUHoycmE5aEMwYjBSeDRFZVJjbzVzbzkifQ.E_wL6zKWzqwHun0nszKsdiddt1fZVxeI6JPY2vrhPmf-j7nQVytuLBliWuZTSjX_X9I2sZTQJ-NoEWu6P7vXjcJky2mbYX31AU0aU0MQ4kFM9Kb2h6VZtnE-7Fv9WipuEz4BJZ1gbo5LU4jku0ZFvIVEwfMFKJ9kdDQjlvPd5zIxqEM2wAz0_w_msTnIxc_LPBw0BQ0iAKNZxBMjgmX6cqObuX5zvPiml7tkUd-oQKktE1rs4doMBacKVHwLbj4EBANCMgBAwL_-cCCXtOszVreoXFo_kcfjVBFMnIQN5q5jxerRE86VNwPazTjoDzj860ulGIg9vFxeBdJn74JKwA'}
    categoryData = {'query_selector': categorySelectorQuery,
                    'html': str(htmlContent)}
    listOfCategories = []
    try:
        categoryResponse = requests.post(
            'https://172.16.250.234:7070/api/v1/cheerio', headers=access_token, json=categoryData)
        try:
            print(categoryResponse)
            listOfCategories = categoryResponse.json()['data']
            listOfCategories.insert(
                0, 'LIST OF CATEGORIES')
        except KeyError as e:
            print("No Output recieved")
            print(e)
            print(categoryResponse.json())
    except:
        print("Bad Response")
    return listOfCategories


def getQnAWithNPL(url):
    tools = Utility()
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    htmlText = tools.textFromHtml(content)
    sentences = tools.SentenceTokenizer(htmlText)
    dictOfQnA = tools.fetchQnAWithHtmlText(sentences)
    category = tools.get_website_name_from_url(url)
    QnAFinal = []
    for keys in dictOfQnA:
        QnAFinal.append({"category": url, "answer": ftfy.fix_text(
            dictOfQnA[keys].strip()[2:]), "question": ftfy.fix_text(keys.strip())+"?"})
    return QnAFinal


def getQnAWithHierarchy(url):
    ### Utility Functions Class Initialized ###
    try:
        tools = Utility()
        content = requests.get(url)
        soup = BeautifulSoup(content.text, 'html.parser')
        htmlText = tools.textFromHtml(content)
        # print(htmlText)
        sentences = tools.SentenceTokenizer(htmlText)
        QnA = tools.fetchQnAWithHtmlText(sentences)
        # pprint(QnA)
        QnAHeirarchies = tools.fetchHtmlHierarchy(QnA, content)
        # pprint(QnAHeirarchies)

        try:
            QnAselectorQueries = tools.generateSelectorQuery(
                QnAHeirarchies[0], QnAHeirarchies[1])
            for x in QnAselectorQueries:
                print(x)
        except IndexError as e:
            # print(e)
            print("COULDN'T FETCH HTML HEIRARCHY")
            return []

        listOfQuestions = getQuenstionsFromQuery(QnAselectorQueries[0], soup)
        listOfAnswers = getAnswersFromQuery(QnAselectorQueries[1], soup)
        dictOfQuestionsAndAnswers = {}
        for question, answer in zip(listOfQuestions, listOfAnswers):
            dictOfQuestionsAndAnswers[question] = answer

        finalListOfQuestionsAndAnswers = []
        category = tools.get_website_name_from_url(url)

        for keys in dictOfQuestionsAndAnswers:
            finalListOfQuestionsAndAnswers.append(
                {"category": url, "answer": ftfy.fix_text(dictOfQuestionsAndAnswers[keys].strip()), "question": ftfy.fix_text(keys.strip())})

        pprint(finalListOfQuestionsAndAnswers)
        print(tools.get_website_name_from_url(url))

        return finalListOfQuestionsAndAnswers
        # fb.setData(user, category.upper(), finalListOfQuestionsAndAnswers)
    except:
        return []

    """ This section of code is for FILE I/O """
    # finalListOfQuestionsAndAnswers.insert(
    #     0, ['Category', 'Answers', 'Questions'])

    # filename = 'QnA' + \
    #     tools.get_website_name_from_url(url) + '.csv'
    # filepath = os.path.join(
    #     'D:\Learning\Python\Scrappy\Downloads', filename)
    # if not os.path.exists('D:\Learning\Python\Scrappy\Downloads'):
    #     os.makedirs('D:\Learning\Python\Scrappy\Downloads')

    # with open(filepath, 'w', newline='', errors='ignore') as csvFile:
    #     wr = csv.writer(csvFile)
    #     for data in finalListOfQuestionsAndAnswers:
    #         wr.writerow(data)
    #     if(category_tag):
    #         wr.writerow(listOfCategories)


def firebaseTesting():
    fb = firebaseUtil()
    user = fb.firebaseAuth()
    fb.getData("IMI")


# getQnAWithHierarchy(url)

# firebaseTesting()
