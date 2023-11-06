import replicate
output = replicate.run(
  "meta/codellama-7b-instruct:7bf2629623162c0cf22ace9ec7a94b34045c1cfa2ed82586f05f3a60b1ca2da5",
  input={
    "top_k": 250,
    "top_p": 0.95,
    "prompt": "Write a javascript function that calculates euclidean distance between two coordinates of any dimension",
    "max_tokens": 500,
    "temperature": 0.95,
    "system_prompt": "",
    "repeat_penalty": 1.1,
    "presence_penalty": 0,
    "frequency_penalty": 0
  }
)
for i in output:
    print(i,end= "")