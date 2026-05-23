from db import supabase
import random

def movie_rec(userid):

    response=supabase.table("movierec_usermovies").select("*").eq("USER ID",userid).execute()

    genres = [g["GENRE"] for g in response.data]
    titlelist=[t["TITLE"] for t in response.data]
    
    if not genres:
        print("No Movies watched yet!")
    else:
         favorite = max(set(genres), key=genres.count)

    mov=supabase.table("movierec_allmovies").select("*").eq("GENRE",favorite).execute()
    if not mov.data:
        print("No reccomendations available for your favourite Genre. ")

    recommendation=[]
    for m in mov.data:
        if m["TITLE"] not in titlelist:
            recommendation.append(m["TITLE"])

    if not recommendation:
        print("No new movies left to recommend!")
        return

    reco=random.choice(recommendation)



    print("The movie recommended to you: ")
    print(reco)