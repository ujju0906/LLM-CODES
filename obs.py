import requests

API_URL = "https://api-inference.huggingface.co/models/NousResearch/Obsidian-3B-V0.5"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
"inputs": "what is photosynthesis? give normal explanation in 50 words","parameters" : {"max_new_tokens": 256}
})
print(output)