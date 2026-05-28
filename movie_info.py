from omdb import get_movie

def get_movie_info(title): 
    response=get_movie(title)

    if response["Response"]=="False":
        print("Movie not found!")
        return
    else:
        print("MOVIE DETAILS: ")
        print("Title: ",response["Title"])
        print("Genre: ",response["Genre"])
        print("IMDb Rating: ",response["imdbRating"])
        print("Actors: ",response["Actors"])
        print("Plot: ",response["Plot"])

