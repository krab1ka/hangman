from random import randint

words = ["loco"]

stages = ["",
          "______       ",
          "|     |      ",
          "|     O      ",
          "|    /|\\    ",
          "|    / \\    ",
          "|____________",
          ]

random = randint(0, (len(words) - 1))
word = list(words[random])
word_compare = list(words[random])

word_cipher = ["_"] * len(word)

print("""-------------------------
|                       |
|     !Поле чудес!      |
|                       |
-------------------------
      
  {}
      """.format(word_cipher))


while len(stages) > 0:
    user = input("Enter char: \n")

    if user in word:
        index_char = word.index(user)
        word_cipher[index_char] = word_compare[index_char]
        word[index_char] = '_'
        print(word_cipher)
        print("")
        
        if word_cipher == word_compare:
            print("""-------------------------
            |                       |
            |   !!!Ты победил!!!    |
            |                       |
            -------------------------
                
            """)
            break
    else:
        stages.pop(-1)
        for i in stages:
            print(i)

if word_cipher != word_compare:
    print("""-------------------------
|                       |
|   !!!Ты Проиграл!!!   |
|                       |
-------------------------
      
""")








