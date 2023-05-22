import requests

def convertToValue(cardValue):
    valueDict = {"JACK": 11, "QUEEN": 12, "KING": 13, "ACE": 14}
    if cardValue in valueDict:
        return valueDict[cardValue]
    return int(cardValue)


response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
log = response.json()
deck_id = log["deck_id"]
print(response.status_code)
print(log)
print(deck_id)

drawCardsResponse = requests.get("https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=2")
drawnCards = drawCardsResponse.json()
#print(drawCardsResponse.json())


value_card_1 = drawnCards['cards'][0]['value']
value_card_2 = drawnCards['cards'][1]['value']


if convertToValue(value_card_1) > convertToValue(value_card_2):
    print("Player 1 wins with a " + value_card_1 + " of " + drawnCards['cards'][0]['suit'] + "!")
elif convertToValue(value_card_2) > convertToValue(value_card_1):
    print("Player 2 wins with a " + value_card_2 + " of " + drawnCards['cards'][1]['suit'] + "!")
elif convertToValue(value_card_1) == convertToValue(value_card_2):
    print("TIE! Both players drew a " + value_card_1)



print("card 1: " + value_card_1 +", card 2: " + value_card_2)
