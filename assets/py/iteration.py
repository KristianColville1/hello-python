data = {
	"first_name": "brian",
	"last_name": "johnson",
	"occupation": "student"
}

scores = [6, 9, 8, 7, 8, 9]

# iteration with key value pairs using the items method.
for key, value in data.items():
    if value is not 'student':
        data[key] = value.capitalize()
        

print(data)

# iteration using the range and len functions 
for i in range(len(scores)):
    scores[i]+=1


print(scores)

# compprehensions - dictionary example

cards = ['king', 'queen', 'jack', 'ace']

cards_dict = {card:card.upper() for card in cards}
print(cards_dict)