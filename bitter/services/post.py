from database.storage import users, posts, Post

FORBIDDEN_WORDS = ["faggot", "nigger", "nigga", "chink", "kike", "retard", "cunt", "tranny","fuck","shit", "bitch"]

def create_post(author:str, content:str) -> bool:
    """
    Create a new post after validation.

    Returns True if successful, False otherwise.
    """
    if author not in users:
        return False
    if not _validate(content):
        return False
    post_id = 1
    if posts:
        post_id = posts[-1]["id"] + 1
    post: Post = {
        "id": post_id,
        "author": author,
        "content": content,
        "likes": [],
        "comments": [],
        "views": 0
    }
    posts.append(post)
    users[author]["posts"].append(post_id)
    return True

def remove_post(author: str,remove_id: str) -> bool:
    """
    Remove post after validation.

    Returns True if successful, False otherwise.
    """
    global posts
    for post in posts:
        if post['id'] == remove_id:
            if post['author'] == author:
                post_to_remove = post
                break 
            else:
                print("You can't delete someone else's post")
                return False
    if not post_to_remove:
        return False
    posts.remove(post_to_remove)
    if remove_id in users[author]['posts']:
        users[author]['posts'].remove(remove_id)
    return True

def edit_post(author: str, edit_id: str, edited_post: str) -> bool:
    """
    Edit post of an existing post if the author matches.

    Returns True if successful, False otherwise.
    """
    global posts
    for post in posts:
        if post['id'] == edit_id:
            if post['author'] == author:
                post_to_edit = post
                break 
            else:
                print("You can't edit someone else's post")
                return False
    if not post_to_edit:
        return False
    post_to_edit['content'] = edited_post
    return True

def post_views(post_id: int) -> bool:
    """
    Add a view if you view the post. 

    Returns True if successful, False otherwise.
    """
    global posts
    for post in posts:
        if post["id"] == post_id:
            post["views"] += 1
            break
    return True

def subscribe_to_user(current_user: str, author: str) -> bool:
    """
    Subscribes the current user to selected author.

    Return True if successful, False if author doesn't exist or already subscribed.
    """
    global users
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

def unsubscribe_to_user(current_user: str, author: str) -> bool:
    """
    Unsubscribes the current user to selected author.

    Return True if successful, False if author doesn't exist or already unsubscribed.
    """
    global users
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

def show_user(author: str, current_user: str) -> bool:
    """Shows user profile details: followers, followings and posts.
    
    Offers an option to subscribe or unsubcribe
    """
    global users,posts
    if author not in users:
        print("User doesn`t exist.")
        return False
    print(f"\n----- {author} -----")
    print(f"Name: {users[author]['name']}\nFollowers: {users[author]["followers"]}\nFollowing: {users[author]["following"]}")
    has_post = False
    for post in posts:
        if post['author'] == author:
            post_views(post['id'])
            print(f"{author}: {post['content']} | Views: {post['views']}")
            has_post = True
    if not has_post:
        print("Has no posts")
    is_subscribed = current_user in users[author]["followers"]
    if is_subscribed:
        action = input(f"You are following {author}. Unsubscribe? (y/n): ").lower() == "y"
        if action:
            unsubscribe_to_user(current_user, author)
    else:
        action = input(f"Would you like to subscribe to {author}? (y/n): ").lower() == "y"
        if action:
            subscribe_to_user(current_user, author)
    return True

def _validate(content: str, max_lenght:int = 280) -> bool:
    """Validates post content: ensures it's not empty, under 280 chars and clean of forbidden words."""
    if not content:
        return False
    if any(word in FORBIDDEN_WORDS for word in content):
        return False
    if len(content) > 280:
        return False  
    return True

_MAX_CONTENT_LENGHT = 280 