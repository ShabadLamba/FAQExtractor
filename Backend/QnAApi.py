from flask import Flask, jsonify, request, render_template, redirect
from flask_cors import CORS
from QnAMain import *
import logging
from Authentication import auth

app = Flask(__name__, static_folder='static',
            template_folder='static')
CORS(app, resources={r'/v2/faq*': {"origins": "*"},
                     r'/v1/faq*': {"origins": "*"}})

### Fire Initialization ###
fb = firebaseUtil()

# fb.setData(user, category.upper(), finalListOfQuestionsAndAnswers)


@app.route('/faq/callback')
@app.route('/faq/extract')
@app.route('/faq/home')
@app.route('/faq/')
@app.route('/faq')
@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/callback')
# def authentication():
#     return redirect('/')

############################ v1 ####################################
@app.route('/v1/faq/extractByUrl/Hierarchy', methods=["POST"])
def fetchByUrl_Hierarchy():
    print(request.get_json())
    tools = Utility()
    req_data = request.get_json()
    try:
        if(req_data and (tools.decryptUrl((req_data["access_token"].encode())).decode()) == "paxzibydpdztcbiicgndskzgpqnicm"):
            user = fb.firebaseAuth()  # Authenticating Firebase
            QnADict = getQnAWithHierarchy(req_data["url"])
            if(len(QnADict) != 0):
                qnaCollectionOrderedDict = fb.getData()
                listOfKeys = []
                for key in qnaCollectionOrderedDict:
                    listOfKeys.append(key)
                listOfUrls = []
                for keys in listOfKeys:
                    # print(listOfKeys[])
                    listOfUrls.append(tools.decryptUrl(keys.encode()).decode())
                if(req_data["url"] not in listOfUrls):
                    fb.setData(user, tools.encryptUrl(
                        req_data["url"]).decode(), QnADict)
                return jsonify(QnADict)

            else:
                return {"error": True,
                        "message": "FAQs couldn't be fetched"}
    except:
        return {
            "error": True,
            "message": "Authentication Error"
        }


@app.route('/v1/faq/extractByUrl/NLP', methods=["POST"])
def fetchByUrl_NLP():
    print(request.get_json())
    user = fb.firebaseAuth()  # Authenticating Firebase
    tools = Utility()
    req_data = request.get_json()
    try:
        if(req_data and (tools.decryptUrl((req_data["access_token"].encode())).decode()) == "paxzibydpdztcbiicgndskzgpqnicm"):
            print("Inside")
            QnADict = getQnAWithNPL(req_data["url"])
            print(QnADict)
            return jsonify(QnADict)
    except:
        return {
            "error": True,
            "message": "Authentication Error"
        }


@app.route('/v1/faq/extractByUrl/GetData/Firebase', methods=["POST"])
def fetchByUrl_GetDataFromFirebase():
    tools = Utility()
    user = fb.firebaseAuth()  # Authenticating Firebase
    req_data = request.get_json()
    try:
        if(req_data and (tools.decryptUrl((req_data["access_token"].encode())).decode()) == "paxzibydpdztcbiicgndskzgpqnicm"):
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
    except:
        return {
            "error": True,
            "message": "Authentication Error"
        }
#######################################################################

############################## v2 #####################################
@app.route('/v2/faq/extractByUrl/Hierarchy', methods=["POST"])
@auth.requires_auth
def fetchByUrl_Hierarchy_v2():
    print(request.get_json())
    tools = Utility()
    req_data = request.get_json()
    try:
        # and (tools.decryptUrl((req_data["access_token"].encode())).decode()) == "paxzibydpdztcbiicgndskzgpqnicm"):
        if(req_data):
            user = fb.firebaseAuth()  # Authenticating Firebase
            QnADict = getQnAWithHierarchy(req_data["url"])
            if(len(QnADict) != 0):
                qnaCollectionOrderedDict = fb.getData()
                listOfKeys = []
                for key in qnaCollectionOrderedDict:
                    listOfKeys.append(key)
                listOfUrls = []
                for keys in listOfKeys:
                    # print(listOfKeys[])
                    listOfUrls.append(tools.decryptUrl(keys.encode()).decode())
                if(req_data["url"] not in listOfUrls):
                    fb.setData(user, tools.encryptUrl(
                        req_data["url"]).decode(), QnADict)
                return jsonify(QnADict)

            else:
                return {"error": True,
                        "message": "FAQs couldn't be fetched"}
    except:
        return {
            "error": True,
            "message": "Authentication Error"
        }


@app.route('/v2/faq/extractByUrl/NLP', methods=["POST"])
@auth.requires_auth
def fetchByUrl_NLP_v2():
    print(request.get_json())
    user = fb.firebaseAuth()  # Authenticating Firebase
    req_data = request.get_json()
    try:
        # and (tools.decryptUrl((req_data["access_token"].encode())).decode()) == "paxzibydpdztcbiicgndskzgpqnicm"):
        if(req_data):
            QnADict = getQnAWithNPL(req_data["url"])
            return jsonify(QnADict)
    except:
        return {
            "error": True,
            "message": "Authentication Error"
        }


@app.route('/v2/faq/extractByUrl/GetData/Firebase', methods=["POST"])
@auth.requires_auth
def fetchByUrl_GetDataFromFirebase_v2():
    tools = Utility()
    user = fb.firebaseAuth()  # Authenticating Firebase
    req_data = request.get_json()
    try:
        # and (tools.decryptUrl((req_data["access_token"].encode())).decode()) == "paxzibydpdztcbiicgndskzgpqnicm"):
        if(req_data):
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
    except:
        return {
            "error": True,
            "message": "Authentication Error"
        }
###################################################################################


@app.route("/faq/heartbeat", methods=["GET"])
def get_heartbeat():
    return jsonify({"Status": "Running"}), 200


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
