import random
import json

import torch

from model import NeuralNet
from main import bag_of_words, tokenize

device = torch.device('cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "BayMax"
print("Let's chat! (type 'quit' to exit)")
while True:
    # sentence = "do you use credit cards?"
    sentence = input("You: ")
    if sentence == "quit":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
                if tag == 'game':
                    # This is where you add the games
                    # add the name into the list
                    # add file to this folder
                    # acc to number, import said file and execute
                    # my games are under a function, making it easier to execute
                    games = ['Hangman', 'Rock Paper Scissor', 'Math Quiz', 'Riddles', 'Jumbled Words']
                    count = 1
                    print('Choose from the following games ')
                    for i in games:
                        print(count, i)
                        count += 1
                    x = int(input('= '))
                    if x == 1:
                        import Hangman

                        Hangman.main()
                    elif x == 2:
                        import rock_paper_scissor as r

                        r.main()
                    elif x == 3:
                        import Math_quiz as m

                        m.main()
                    elif x == 4:
                        import riddles as r

                        r.main()
                    elif x == 5:
                        import jumbled_words as j

                        run1 = True
                        while run1:
                            j.main()
                            xy = input('Do you want another round?(Y/N) = ')
                            if xy in 'nN':
                                run1 = False
                                break

                    print(f"{bot_name}: Hope you had fun playing")
    else:
        tag = "generic"
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
