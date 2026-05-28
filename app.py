from auth import signup, login
from ratings import add_rating
from recomendation import movie_rec
from movie_info import get_movie_info
from db import supabase

while True:
 print("1. Signup")
 print("2. Login")
 print("3. Exit")

 choice = input("Choose: ")

 if choice == "1":

    username = input("Username: ")
    email=input("Email: ")
    password = input("Password: ")

    signup(email,password,username)

    


 elif choice == "2":
    
    email = input("Email: ")
    password = input("Password: ")

    user = login(email,password)
    
    if not user:
        print("Invalid login") 
        

    else:
        
        profile = supabase.table("movierec_users").select("*").eq("EMAIL", email).execute()
        user_id = profile.data[0]["USER ID"]
        username = profile.data[0]["USERNAME"]


        while True:

         print("1. Add Review")
         print("2. Get Recommendation")
         print("3. Get Information about Movie")
         print("4. Logout")

         action = input("Choose: ")

         if action == "1":

            title = input("Movie title: ")
            rating = int(input("Rating (1-5): "))

            add_rating(
                user_id,
                title,
                rating
            )

         elif action == "2":

            movie_rec(user_id)

         elif action=="3":
            title=input("Enter Title: ")
            get_movie_info(title)
         else:
            break
   
 else:
   print("See you again!")
   break