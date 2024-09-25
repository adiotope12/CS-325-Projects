from llama_cpp import Llama

#Connect to the llm using the huggingface repo and the file downloaded locally.
llm = Llama.from_pretrained(
	repo_id="microsoft/Phi-3-mini-4k-instruct-gguf",
	filename="Phi-3-mini-4k-instruct-fp16.gguf",
)

#Opens the prompt file and the output file.
f1 = open("Prompts.txt", "r",encoding="utf-8")
f2 = open("Answers.txt", "w+",encoding="utf-8")

#Get first prompt and begin looping through the rest.
read = f1.readline()
x = 0
while(read != ""):
	x += 1
	#Send the prompt to the llm and get the response.
	temp = llm.create_chat_completion(
		messages = [
			{
			"role": "user",
			
			"content": str(read)
			}
		]	
	) 
	#Write the response to the output file.
	f2.write(str(x)+". ")
	f2.write(read + "\n")
	f2.write(temp["choices"][0]["message"]["content"])
	f2.write("\n\n")

	#Get the next prompt from the prompt file.
	read = f1.readline()

#Close the prompt and output files.
f1.close()
f2.close()
