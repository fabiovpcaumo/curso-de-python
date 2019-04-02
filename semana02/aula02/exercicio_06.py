

def filter_users(list_users : list) -> tuple:
    filtered_users = []
    
    for user in list_users:
        if user != ():
            if user[0] > 100:
                filtered_users.append(user)
                
    return filtered_users
        