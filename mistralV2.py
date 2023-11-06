import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
"inputs": "what is photosynthesis? give normal explanation in 50 words","parameters" : {"max_new_tokens": 256}
})
print(output[0]['generated_text'])