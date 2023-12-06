"""
Author: Flávio Tomé - flavio.tome@orbitdatascience.com
Date: 2023-09-18

This is a basic template for a web app backend.
It runs using a Flask framework, executing within a Docker Container
configurated to run on port 5000.



"""
from flask import Flask, jsonify, request
from flask_cors import CORS
import io
import pandas as pd

from scripts import getTest, calculateTotal

# The CORS extension is applied to the Flask app.
# This is important for handling cross-origin requests,
# allowing the frontend, hosted on a different domain,
# to interact with this backend.
app = Flask(__name__)
CORS(app)


#  An endpoint is defined at the root URL ("/")
#  using the @app.route decorator.
#  This route only handles HTTP GET requests
#  and responds with a JSON message saying,
#  "Orbit Web Template says: Backend here!".
@app.route("/", methods=['GET'])
def index():

    return jsonify("Orbit Web Template says: Backend here!")

# This route can handle both GET and POST requests.
# It calls the getTest function, passing in some parameters,
# and returns the result as a JSON object.
@app.route("/test", methods=['GET','POST'])
def test():

    dataFrame = getTest(2,4)
    return jsonify(dataFrame.to_json(orient = "split"))


@app.route("/api/gettotal", methods=['GET','POST'])
def getTotal():
    #get the data from frontend      
    json_data = request.get_json()

    #get the first list of json file to set the dataframe columns        
    columns = json_data[0]
    #set the dataframe data
    data = json_data[1:]

    df = pd.DataFrame(data, columns=columns)

    final_df = calculateTotal(df)
    #final_df.to_excel("teste2.xlsx")
    final_json = final_df.to_json(orient='records')

    return jsonify(final_json)

# the Flask app is started with the host set to '0.0.0.0'
# (meaning it listens on all available network interfaces)
# and port 5000.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
