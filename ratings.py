from db import supabase


def update_rating(title):
    response=supabase.table("movierec_usermovies").select("*").eq("TITLE",title).execute()
    ratings = [r["RATING"] for r in response.data]

    avg=sum(ratings)/len(ratings)
    supabase.table("movierec_allmovies").update({
        "AVERAGE RATING":avg}).eq("TITLE",title).execute()


def add_rating(user_id,title, genre, rating):
    title=title.strip().title()
    genre=genre.strip().title()
    data={
        "USER ID":user_id,
        "TITLE": title,
        "GENRE": genre,
        "RATING": rating
    }
    try:
        supabase.table("movierec_usermovies").insert(data).execute()
    
    except:
        print("Already rated the movie!")


    existing=supabase.table("movierec_allmovies").select("*").eq("TITLE",title).execute()

    if not existing.data:
        moviedata={
            "TITLE":title,
            "GENRE":genre,
            "AVERAGE RATING":rating
        }

        supabase.table("movierec_allmovies").insert(moviedata).execute()

    else:
        update_rating(title)
        
    print("Reviewed Sucessfully!")

