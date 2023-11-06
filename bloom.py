#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
import requests

API_URL = "h"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "what is photosynthesis ?","parameters" : {"max_new_tokens": 256}
})
print(output[0]['generated_text'])