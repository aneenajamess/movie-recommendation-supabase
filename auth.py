from db import supabase

def signup(email, password,username):
    try: 
        data=supabase.auth.sign_up({
            "email":email,
            "password":password
            })
        user=data.user
        
        if not user:
            print("Signup Failed")
            return
        
        dat={
            "user_id":user.id,
            "USERNAME":username,
            "EMAIL": email,
            }
        supabase.table("movierec_users").upsert(dat).execute()
        print("Signup successful!")
        print("\n")
    except:
        print("Profile already exists!")

def login(email,password):
    data=supabase.auth.sign_in_with_password({
        "email":email,
        "password":password
    })

    user =data.user
    return user