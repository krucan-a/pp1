reduta = """Nam strzelać nie kazano. Wstąpiłem na działo.
 I spojrzałem na pole, dwieście armat grzmiało.
 Artyleryji ruskiej ciągną się szeregi,
  Prosto, długo, daleko, jako morza brzegi"""
def samogloski(tekst):
    import re
    return len(re.findall('[aeiouyAEIOUY]',tekst))
print("Ilość samogłosek wynosi: ", samogloski(reduta))