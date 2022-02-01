movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def worthIt(selection):
  for movie in movies:
    if movie["name"] == selection:
      if movie["imdb"] > 5.5:
        print(f'{movie["name"]} is worth it and the score is {movie["imdb"]}')
      else:
        print('no')


def score():
  for movie in movies:
    if movie["imdb"] > 5.5:
      print(movie["name"], movie["imdb"])

def genre(selection):
  for movie in movies:
    if movie["category"] == selection:
      print(movie["name"])

def average(movieList):
  averageList = 0
  movieTotal = 0
  for item in movieList:
      for movie in movies:
        if movie["name"] == item:
          averageList += movie['imdb']
          movieTotal += 1
  return averageList/movieTotal

def genreAverage(selection):
  averageList = 0
  movieTotal = 0
  for movie in movies:
    if movie["category"] == selection:
      averageList += movie["imdb"]
      movieTotal += 1
  return averageList/movieTotal

print(genreAverage("Thriller"))

#My VSCode was extremely slow when attempting to do this so im sharing on a repl hopefully it works the same.