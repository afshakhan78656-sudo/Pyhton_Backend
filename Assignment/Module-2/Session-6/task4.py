titles=["Pathan"," 3 Idiots","P.K"]
genres = ["Action","Comedy", "Comedy"]
ratings = [8.5, 7.0, 8.4]

movies=[]

for titles,genres,ratings in zip(titles,genres,ratings):
    movie={
        "title":titles,
        "genre":genres,
        "rating":ratings
    }

    movies.append(movie)

print(movies)