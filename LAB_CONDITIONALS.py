movie:str="The Shawshank Redemption"
rating_of_the_movie:int=3
popularity_score:float=72.65
if rating_of_the_movie >=4 and popularity_score>80:
    print("Highly recommended")
elif rating_of_the_movie >=3 and popularity_score>70:
    print("I recommended it . It is good")
elif rating_of_the_movie <=2 and popularity_score>60:
    print("You should check it out!")
else:
    print("Don't watch it. It is a waste of time")
