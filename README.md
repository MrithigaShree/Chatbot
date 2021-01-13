# Chatbot
This is Baymax. Except all he does it play games, jokes around, and occasionally roasts you.

# Installation
### Create an environment - conda or venv

mkdir myproject

`$ cd myproject`
`$ python3 -m venv venv `

### Activate it
#### Mac / Linux:

* venv/bin/activate
#### Windows:

* venv\Scripts\activate

### Install PyTorch and dependencies
For Installation of PyTorch see official website.

### You also need nltk:

pip install nltk
If you get an error during the first run, you also need to install nltk.tokenize.punkt: Run this once in your terminal:

$ python  
`import nltk`  
`nltk.download('punkt')`

### Run

python train.py
This will dump the new data in to the data.ph file

python chat.py
### Customize
Have a look at intents.json. You can customize it according to your own use case. Just define a new tag, possible patterns, and possible responses for the chat bot. You have to re-run the training whenever this file is modified.

I have used multiple text-files for the games as this was a school project, which requires usage of text files. Feel free to modify the code to your liking.

