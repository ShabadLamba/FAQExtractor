from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from QnAMain import *
import logging


app = Flask(__name__, static_folder='static',
            template_folder='static')
CORS(app, resources={r'/faq/extractByUrl/*': {"origins": "*"}})

### Fire Initialization ###
fb = firebaseUtil()
user = fb.firebaseAuth()  # Authenticating Firebase

# fb.setData(user, category.upper(), finalListOfQuestionsAndAnswers)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/faq/extractByUrl/Hierarchy', methods=["POST"])
def fetchByUrl_Hierarchy():
    print(request.get_json())
    tools = Utility()
    req_data = request.get_json()
    QnADict = getQnAWithHierarchy(req_data["url"])
    fb.setData(user, tools.encryptUrl(req_data["url"]).decode(), QnADict)
    return jsonify(QnADict)


@app.route('/faq/extractByUrl/NLP', methods=["POST"])
def fetchByUrl_NLP():
    print(request.get_json())
    req_data = request.get_json()
    QnADict = getQnAWithNPL(req_data["url"])
    return jsonify(QnADict)


@app.route('/faq/extractByUrl/GetData/Firebase', methods=["POST"])
def fetchByUrl_GetDataFromFirebase():
    tools = Utility()
    req_data = request.get_json()
    qnaCollectionOrderedDict = fb.getData()
    listOfKeys = []
    for key in qnaCollectionOrderedDict:
        listOfKeys.append(key)
    listOfUrls = []
    for keys in listOfKeys:
        # print(listOfKeys[])
        listOfUrls.append(tools.decryptUrl(keys.encode()).decode())
    for url in listOfUrls:
        if(url == req_data["url"]):
            return jsonify(qnaCollectionOrderedDict[listOfKeys[listOfUrls.index(url)]])
    return jsonify([False])


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request. %s', e)
    return "An internal error occured", 500

# @app.route('/faq/extractByUrl/Questions', methods=["POST"])
# def fetchByUrl_Questions():
#     return


# @app.route('/faq/extractByUrl/Answers', methods=["POST"])
# def fetchByUrl_Answers():
#     return


# @app.route('/faq/extractByUrl/Categories', methods=["POST"])
# def fetchByUrl_Categories():
#     return


# @app.route('/faq/extractByUrl/GetQuestionsHierarchy', methods=["POST"])
# def fetchByUrl_GetQuestionsHierarchy():
#     return


# @app.route('/faq/extractByUrl/GetAnswersHierarchy', methods=["POST"])
# def fetchByUrl_GetAnswersHierarchy():
#     return

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
