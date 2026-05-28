from db import supabase
from omdb import get_movie


def update_rating(title):
    titlekey=title.strip().lower()
    response=supabase.table("movierec_usermovies").select("*").eq("TITLE_KEY",titlekey).execute()
    ratings = [r["RATING"] for r in response.data]

    avg=sum(ratings)/len(ratings)
    supabase.table("movierec_allmovies").update({
        "AVERAGE RATING":avg}).eq("TITLE_KEY",titlekey).execute()


def add_rating(user_id,title,rating):
    moviedata=get_movie(title)
    if moviedata["Response"]=="False":
        print("Movie not found!")
        return
    else:
        title=moviedata["Title"]
        genre=moviedata["Genre"]

    titlekey=title.strip().lower()
    
    data={
        "USER ID":user_id,
        "TITLE": title,
        "TITLE_KEY":titlekey,
        "GENRE": genre,
        "RATING": rating
    }
    try:
        supabase.table("movierec_usermovies").insert(data).execute()
    
    except:
        print("Already rated the movie!")


    existing=supabase.table("movierec_allmovies").select("*").eq("TITLE_KEY",titlekey).execute()

    if not existing.data:
        moviedata={
            "TITLE":title,
            "TITLE_KEY":titlekey,
            "GENRE":genre,
            "AVERAGE RATING":rating
        }

        supabase.table("movierec_allmovies").insert(moviedata).execute()

    else:
        update_rating(title)
        
    print("Reviewed Sucessfully!")



"""input moviename-> 
checkif movie exists->
if yes fetch details->
check if movie alr there in movierec usermovies->
else add it to movirec usermovies-> 
check if its there in all movies, if no add it there asw, -> 
else update rating"""