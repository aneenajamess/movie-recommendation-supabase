from auth import signup, login
from ratings import add_rating
from recomendation import movie_rec
while True:
 print("1. Signup")
 print("2. Login")
 print("3. Exit")

 choice = input("Choose: ")

 if choice == "1":

    username = input("Username: ")
    password = input("Password: ")

    signup(username, password)

 elif choice == "2":
    

    username = input("Username: ")
    password = input("Password: ")

    user = login(username, password)

    if not user:
        print("Invalid login") 

    else:
        while True:

         print("Welcome", user["USERNAME"])

         print("1. Add Review")
         print("2. Get Recommendation")
         print("3. Logout")

         action = input("Choose: ")

         if action == "1":

            title = input("Movie title: ")
            rating = int(input("Rating (1-5): "))

            add_rating(
                user["USER ID"],
                title,
                rating
            )

         elif action == "2":

            movie_rec(user["USER ID"])
         else:
            break
 else:
    break