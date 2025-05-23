# Sentence-Rewriter
This project rewrites a given input sentence in a tone selected by the user, making use of NLP and ML.
In the program, we make use of flask for making it a webapp and provide a simple yet pleasant user-interface using the powers of html and css.
Here, when the user inputs the sentence, selects the tone and clicks the "Rewrite" button, here's what happens, the user input is tokenized and the raw data is converted into json format and is then sent to the model via an in-built prompt present in the program, the model then runs and gives a similar sentence but based on the tone (classified based on word embeddings). This response then decoded again and returned back in the output container.
This program, makes use of NLP and ML to implement a concept called style-transfer.
The tones provided here are: Apologetic, Agressive, Formal, Casual, GenZ and Flirty. Which can be changed as per requirement just by changing it in the HTML file.

# How to run the program:
After cloning and all the files are in the system. Run the app.py file and the program should open in a browser tab just fine.
Enter the input sentence and select the desired tone. Click the "Rewrite" button and get the output.
**Note: Ensure there is a stable internet Connection since the program has to send the prompt to the model and recieve a response.
