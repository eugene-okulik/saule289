text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
format_list = text.split()
text_list = []
#print(format_list)
for word in format_list:
    if word.endswith(',') or word.endswith('.'):
        new_word = word[:-1] + 'ing' + word[-1]
    else:
        new_word = word + 'ing'
    text_list.append(new_word)
new_text = ' '.join(text_list)
print(new_text)