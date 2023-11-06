import replicate
output = replicate.run(
  "meta/codellama-34b-instruct:bf86bd92b9dfc81992d7e4ed4c890a3693819d437279a077a9259675048370d1",
  input={
    "prompt": "Write a python function that sums 2 integers together, and returns the result.",
    
    "system_prompt": "Responses should be written in python."
    
  }
)
for i in output:
    print(i, end="")