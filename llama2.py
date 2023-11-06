import replicate
output = replicate.run(
    "meta/llama-2-7b-chat:13c3cdee13ee059ab779f0291d29054dab00a47dad8261375654de5540165fb0",
    input={"prompt": "how does an IC engine work ","max_new_tokens":1000}
)
# The meta/llama-2-7b-chat model can stream output as it's running.
# The predict method returns an iterator, and you can iterate over that output.
for item in output:
    ## https://replicate.com/meta/llama-2-7b-chat/versions/13c3cdee13ee059ab779f0291d29054dab00a47dad8261375654de5540165fb0/api#output-schema
    print(item, end="")
#print(output)