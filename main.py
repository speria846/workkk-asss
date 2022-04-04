import random
Sentence_starter = ['About 100 years ago', ' In 1990s', 'Once upon a time']

character = [' there lived a man called Kibwetere.', ' there was a man named Kibwetere.',
             ' there lived a man called Kibwetere.']

time = [' One day', ' One time']

story_plot = [' he was passing moving around ', ' he was going to the garden ', 'he was going to hunt ']

place = [' the swamp', 'the forests']

second_character = [' he saw a baby crying in the swamp', ' he heard a crying baby in the forest']

age = [' who seemed to be two years old', ' who had two years of age']

work = [' he took the  girl to his home and finally the girl got money and changed kibweteres life.']
print(random.choice(Sentence_starter)+random.choice(character) +
      random.choice(time)+random.choice(story_plot) +
      random.choice(place)+random.choice(second_character) +
      random.choice(age) + random.choice(work))