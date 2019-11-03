tekst = "To be, or not to be, that is the question"
import re
samogloski = re.findall('[aeiouyAEIOUY]',tekst)
print(f"Ilość samogłosek wynosi {len(samogloski)}")