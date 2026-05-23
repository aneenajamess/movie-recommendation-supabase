from db import supabase

def signup(username, password):
    data={
        "USERNAME":username,
        "PASSWORD":password
    }

    supabase.table("movierec_users").insert(data).execute()


def login(username,password):
    data={
        "USERNAME":username,
        "PASSWORD":password
    }

    response=(supabase.table("movierec_users").select("*").eq("USERNAME",username).eq("PASSWORD",password).execute())

    if response.data:
        return response.data[0]
    return None