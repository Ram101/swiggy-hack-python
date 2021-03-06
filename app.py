from flask import Flask, jsonify, request
import requests


app = Flask(__name__)

def ResturentListResponse(user_id):
	return  {
            "recipient": {
                   "id": user_id
                 },
                 "message": {
                 "text": "hello, world!"
                  }
           }
    

PAGE_ACCESS_TOKEN_URL = "https://graph.facebook.com/v2.6/me/messages?access_token=EAABpV7CWY9kBAOilkdMKTAZBtfMTVOxP7VtnLb03WBLgk28unT7cD07eQOPoAGZBAcaFsQPpuDtJurl7CU4gHKKhZAzndSMSRe6SA1V6pKUCZAzawOVWzwhSnk5IUxrZBTjmhC5WFt3ZBcNnx6izZBc6zNGzyZA2vxy2EQmWqPZC9lgZDZD"    
ACTION_GET_RESTAURENTS = "order.restaurant"
ACTION_GET_FOOD_FROM_RESTAURANTS = "ordernearme.ordernearme-custom"
ACTION_FOOD_SELECTED_FROM_RESTAURANTS = "order placed for burger from kfc"

@app.route("/swiggyBot", methods=["POST"])
def get_nearbyresturent():
          if not request.json:
          	abort(400)
          print(jsonify(request.json))
          originalRequest = request.json.get("originalRequest")
          source = originalRequest.get("source")
          if source == "facebook":
          	contexts = request.json.get("contexts")
          	results = request.json.get("result")
          	action = results.get("action")
          	data = originalRequest.get("data")
          	recipient = data.get("sender")
          	user_id = recipient.get("id")
          	if action == ACTION_GET_RESTAURENTS:
                          headers = {'Content-type': 'application/json'}
                          requests.post(PAGE_ACCESS_TOKEN_URL,data=ResturentListResponse(user_id),headers=headers)
                          return jsonify(ResturentListResponse(user_id)) ,200
          return 'Sorry please send from a '

			
if __name__ == "__main__":
	app.run(debug=True)
