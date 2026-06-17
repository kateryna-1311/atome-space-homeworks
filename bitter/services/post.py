from database.storage import users, posts, Post

def create_post(author: str, content: str) -> bool:
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
    
def remove_post(posts: list, author: str, post_id: str) -> bool:
    """
    Remove post after validation.

    Returns True if successful, False otherwise.
    """
    for post in posts:
        if post['id'] == post_id:
            if post['author'] != author:
                return False
            posts.remove(post)
            if post_id in users[author]['posts']:
                users[author]['posts'].remove(post_id)
            return True
    return False

def edit_post(posts: list, author: str, edit_id: str, edited_post: str) -> bool:
    """
    Edit post of an existing post if the author matches.

    Returns True if successful, False otherwise.
    """
    for post in posts:
        if post['id'] == edit_id:
            if post['author'] != author:
                return False
    if not post:
        return False
    post['content'] = edited_post
    return True

def post_views(posts: list, post_id: int, current_user: str) -> bool:
    """
    Increment the view count of a post.

    Returns True if successful, False otherwise.
    """
    for post in posts:
        if post["id"] == post_id:
            if post["author"] != current_user:
                post["views"] += 1
                return True
            return False
    return False

def _validate(content: str) -> bool:
    """Validates post content: ensures it's not empty, under 280 chars and clean of forbidden words."""
    if not content:
        return False
    if any(word in _FORBIDDEN_WORDS for word in content):
        return False
    if len(content) > _MAX_CONTENT_LENGHT:
        return False  
    return True

_MAX_CONTENT_LENGHT = 280 
_FORBIDDEN_WORDS = ["faggot", "nigger", "nigga", "chink", "kike", "retard", 
                   "cunt", "tranny","fuck","shit", "bitch"]