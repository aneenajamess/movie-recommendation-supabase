from db import supabase


def update_rating(title):
    titlekey=title.strip().lower()
    response=supabase.table("movierec_usermovies").select("*").eq("TITLE_KEY",titlekey).execute()
    ratings = [r["RATING"] for r in response.data]

    avg=sum(ratings)/len(ratings)
    supabase.table("movierec_allmovies").update({
        "AVERAGE RATING":avg}).eq("TITLE_KEY",titlekey).execute()


def add_rating(user_id,title, genre, rating):
    titlekey=title.strip().lower()
    genre=genre.strip().lower()
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

