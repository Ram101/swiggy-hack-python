from flask import Flask, jsonify, request

app = Flask(__name__)

def ResturentListResponse(user_id):
	return  {
                "speech": "Barack Hussein Obama II was the 44th and current President of the United States.",
                "displayText": "Barack Hussein Obama II was the 44th and current President of the United States, and the first African American to hold the office. Born in Honolulu, Hawaii, Obama is a graduate of Columbia University   and Harvard Law School, where ",
                "data": {
                  "recipient": {
                    "id": user_id
                  },
                  "message": {
                    "attachment": {
                      "type": "template",
                      "payload": {
                        "template_type": "generic",
                        "elements": [
                          {
                            "title": "Welcome to Peters Hats",
                            "image_url": "https://petersfancybrownhats.com/company_image.png",
                            "subtitle": "We have got the right hat for everyone.",
                            "buttons": [
                              {
                                "type": "web_url",
                                "url": "https://petersfancybrownhats.com",
                                "title": "View Website"
                              },
                              {
                                "type": "postback",
                                "title": "Start Chatting",
                                "payload": "DEVELOPER_DEFINED_PAYLOAD"
                              }
                            ]
                          }
                        ]
                      }
                    }
                  }
                },
                "contextOut": "",
                "source": "DuckDuckGo"
              }
    


ACTION_GET_RESTAURENTS = "order.restaurant"
ACTION_GET_FOOD_FROM_RESTAURANTS = "ordernearme.ordernearme-custom"
ACTION_FOOD_SELECTED_FROM_RESTAURANTS = "order placed for burger from kfc"

@app.route("/swiggyBot", methods=["POST"])
def get_nearbyresturent():
	if not request.json:
		abort(400)
	originalRequest = request.json.get("originalRequest")
	source = originalRequest.get("source")
	if source == "facebook":
		contexts = request.json.get("contexts")
		results = request.json.get("result")
		action = results.get("action")
		data = originalRequest.get("data")
		recipient = data.get("recipient")
		user_id = recipient.get("id")
		if action == ACTION_GET_RESTAURENTS :
			return jsonify(ResturentListResponse(user_id)) ,200
	return 'Sorry please send from a '

			
if __name__ == "__main__":
	app.run(debug=True)
