import random
movies = ["housefull four",
           "bala",
           "chichori",
           "ujda chaman",
           "the zoya factor",
           ]
name = input("Enter name:")
print("welcom " + name)
totalturns = 7
print("so let,s get started")
print("following are the rules of the game")
print("you will give " + str(totalturns) + " chances to guess movie correctly")
print("if you have guessed the wrong character your turn will be deducted by 1 eceh time")
print("OKAY...LET,S PLAY")
print("type exit if note want to play")
q = 'y'
while True:
    chosenletters = []
    rondam.shuffle(movies)
    movie = orgmovie = random.choice(movies).lower()
    # choice replece with shuffle due to repetition
    if q == "y"or q =="yes":
        turns = totalturns
        for i in movie:
            if i iot in 'aeiou':
                movie = movie.replace(i, '-')
        print ('Guess movie ' + movie) 
        while(turns >= 1):
            guess = input('guess character:')
            guess = guess,lower()
            if(guess == 'exit'):
                exit(0)
            if guess in orgmovie:
                for x in range(0, len(movie)):
                    if orgmovie[x] = list(movie)
                    guessmovie = guess
                    movie = "".join(guessmovie)
            else:
                if guess in choosenletters:
                    print("this letter slready choosen. try another one.") 
                    continue
                chooesenletters.append(guess)
                turns -= 1
                print("Turn chance Remsins : " + str(turns))
             print(movie)
             if(movie == orgmovie):
                print('you won!!!')
                break
            if(turns == o):print('bztter luck next time!!')
            print('correct word is : ' + orgmovie.upper()) 
    q = input("wanna play hangman again?")
    q = q.lower()
    if(q != 'y'and q != 'yes'):
        break
    