from database.storage import users, User
from services.post import post_views

def create_user(user_name: str) -> bool:
    if any(character in _SPECIAL_CHARACTERS for character in user_name):
        return False
    user: User = {
        'name': user_name,
        'followers': [],
        'following': [],
        'posts':[]
    }
    users[user_name] = user
    return True

def get_current_user() -> str:
    user_name = ""
    while not user_name:
        user_name = input("Your username: ").strip()
    if user_name not in users:
        create_user(user_name)
        print(f"Created a new user: {user_name}")
    else:
        print(f"Welcome back, @{user_name}")
    return user_name

def subscribe_to_user(users: dict, current_user: str, author: str) -> bool:
    """
    Subscribes the current user to selected author.

    Return True if successful, False if author doesn't exist or already subscribed.
    """
    if author not in users:
        print("User not found")
        return False
    if current_user == author:
        print("You cannot subscribe to yourself")
        return False
    if current_user in users[author]["followers"]:
        print(f"You are already subscribed to {author}.")
        return False    
    users[author]["followers"].append(current_user)
    users[current_user]["following"].append(author)
    print(f"Subsctibed to {author}")
    return True

def unsubscribe_to_user(users: dict, current_user: str, author: str) -> bool:
    """
    Unsubscribes the current user to selected author.

    Return True if successful, False if author doesn't exist or already unsubscribed.
    """
    if author not in users:
        print("User not found")
        return False
    if current_user == author:
        print("You cannot unsubscribe to yourself")
        return False
    if current_user not in users[author]["followers"]:
        print(f"You are not subscribed to {author}.")
        return False  
    users[author]["followers"].remove(current_user)
    users[current_user]["following"].remove(author)
    print(f"Unsubscribed from {author}")
    return True

def show_user(posts: list, users: dict, author: str, current_user: str) -> bool:
    """Shows user profile details: followers, followings and posts.
    
    Offers an option to subscribe or unsubcribe
    """
    if author not in users:
        print("User doesn`t exist.")
        return False
    print(f"\n----- {author} -----")
    print(f"Name: {users[author]['name']}\nFollowers: {users[author]["followers"]}\nFollowing: {users[author]["following"]}")
    has_post = False
    for post in posts:
        if post['author'] == author:
            post_views(posts, post['id'], current_user)
            print(f"{author}: {post['content']} | Views: {post['views']}")
            has_post = True
    if not has_post:
        print("Has no posts")
    is_subscribed = current_user in users[author]["followers"]
    if is_subscribed:
        action = input(f"You are following {author}. Unsubscribe? (y/n): ").lower() == "y"
        if action:
            unsubscribe_to_user(users, current_user, author)
    else:
        action = input(f"Would you like to subscribe to {author}? (y/n): ").lower() == "y"
        if action:
            subscribe_to_user(users, current_user, author)
    return True

_SPECIAL_CHARACTERS = "!@#$%^&*()_+-=[]{}|;:,.<>?/"