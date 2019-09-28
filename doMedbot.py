from flask import Flask, escape, request, jsonify, render_template
import joblib
import pandas as pd
import requests
import json

app = Flask(__name__)

#Request route
@app.route('/hello', methods=['GET', 'POST'])
def hello():

    # POST request
    if request.method == 'POST':
        print('Incoming POST request..')
        print(request.get_json())  # parse as JSON
        
        #test payload
        #payload = [1,0,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
        
        #Get Data (Python returns this json as dict)
        jsonData = request.get_json()

        #payload container
        payload =[]

        #stringify to get length of keys
        sanitized_incoming = str(jsonData)
        entryLength = len(jsonData['data'].keys())
        
        #start from question 1
        for entry in range(1, entryLength +1):
            payload.append(jsonData['data']['Question' + str(entry)][0])
        
        print (payload)

        def testModel(payload):
            response=[]
            model_KNN=joblib.load("KNN12_disease.pkl" )
            model_DT=joblib.load("DT_disease.pkl")
            
            test = pd.DataFrame()
            test['running nose'] = [payload[0]]
            test['nasal obstruction'] = [payload[1]]
            test['sneezing'] = [payload[2]]
            test['throat pain'] = [payload[3]]
            test['tiredness'] = [payload[4]]
            test['cough'] = [payload[5]]
            test['fever'] = [payload[6]]
            test['malaise'] = [payload[7]]
            test['inflamed tonsils'] = [payload[8]]
            test['hoarse voice'] = [payload[9]]
            test['breathlessness'] = [payload[10]]
            test['chest pain'] = [payload[11]]
            test['restlessness'] = [payload[12]]
            test['anxiety'] = [payload[13]]
            test['wheezing'] = [payload[14]]
            test['chills'] = [payload[15]]
            test['body ache'] = [payload[16]]
            test['appetite loss'] = [payload[17]]
            test['lethargy'] = [payload[18]]
            test['weight loss'] = [payload[19]]
            test['headache'] = [payload[20]]
            test['memory loss'] = [payload[21]]
            test['sleeplessness'] = [payload[22]]
            test['vomiting'] = [payload[23]]
            test['nausea'] = [payload[24]]
            test['constipation'] = [payload[25]]
            test['rashes'] = [payload[26]]
            test['itching'] = [payload[27]]
            test['joint pain'] = [payload[28]]
            test['swelling'] = [payload[29]]
            test['weakness'] = [payload[30]]
            test['hyper sweating'] = [payload[31]]
            test['swollen gums'] = [payload[32]]
            test['weight gain'] = [payload[33]]
            test['ear pain'] = [payload[34]]
            test['body stiffness'] = [payload[35]]
            test['temperature'] = [payload[36]]
 
            predict_disease = model_KNN.predict(test)
            #print( "The patient should refer to (accoding to KNN model):")
            #print(predict_disease)

            #predict_disease = model_DT.predict(test)
            #print( "The patient should refer to (according to DT model):")
            #print(predict_disease)

            return (predict_disease)

        disease = str(testModel(payload))
         
        return jsonify(disease)

    # GET request
    else:
        message = {'greeting':'Hello from Flask! You have gotten something from the python script using a GET request!'}
        return jsonify(message)  # serialize and use JSON headers

#main page route
@app.route('/main')
def render_page():
    return render_template('Medbot.html')

