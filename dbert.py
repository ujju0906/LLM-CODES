import requests

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-cased-distilled-squad"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": {
		"question": "what is AC motor",
		"context": "An AC motor is a motor that converts alternating current into mechanical power. The stator and the rotor are important parts of AC motors. The stator is the stationary part of the motor, and the rotor is the rotating part of the motor. The AC motor may be single-phase or three-phase. Nikola Tesla invented the first AC induction motor in 1887." 
		
	},
})

print(output)