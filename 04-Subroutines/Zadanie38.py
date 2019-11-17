import re
def capital_letters(text):
    capital_text = ""
    capital_array = []
    capital_array = re.findall("[A-Z]",text)
    for x in capital_array:
        capital_text += x
    return capital_text
text = "AAABbsbadsfbdaSADBBFSBfsabsdgB"
print(capital_letters(text))