from services.user import get_current_user, show_user
from services.post import create_post, remove_post, edit_post, post_views
from database.storage import users, posts


def show_menu(current_user: str) -> None:
    print("\nWelcome to the bitter, where you can write posts!")
    print(f"You are signed in as: {current_user}")
    print("1.Create post")
    print("2.Delete post")
    print("3.Edit post")
    print("4.Look at all posts")
    print("5.Find user's post")
    print("6.Show user")
    print("7.Exit")

def main() -> None:
    current_user = get_current_user()
    show_menu(current_user)
    while True:
        choice = input("What do you want to do?").strip()
        if choice in ('1', 'create post'):
            content = input("Write your posr here: ").strip()
            if create_post(current_user, content):
                print("Your post was created")
            else:
                print("Could not create post. Check the post lenght or forbidden words in it")
        elif choice in ('2', 'delete post'):
            user_posts = [post for post in posts if post["author"] == current_user]
            if user_posts:
                print(f"Your posts:")
                for post in user_posts:
                    print(f"{post['id']}: {post['content']}")
                post_id = int(input("Which post you want to delete?: "))
                if remove_post(posts, current_user, post_id):
                    print("Post was deleted")
                else:
                    print("Could not delete post. Check if the ID is correct")
            else:
                print("You have no posts")    
        elif choice in ('3', 'edit post'):
            user_posts = [post for post in posts if post["author"] == current_user]
            if user_posts:
                print(f"Your posts:")
                for post in user_posts:
                    print(f"{post['id']}: {post['content']}")
                    edit_id = int(input("Which post you want to edit?: "))
                    edited_post = input("Enter edited post: ")
                    if edit_post(posts, current_user, edit_id, edited_post):
                        print("Post was edited")
                    else:
                        print("Could not edit post. Check if the ID is correct")
            else:
                print("You have no posts")       
        elif choice in ('4', 'look at all posts'):
            for author in users:
                print(f"\n----- {author} -----")
                has_post = False
                for post in posts:
                    if post['author'] == author:
                        post_views(posts, post['id'], current_user)
                        print(f"{author}: {post['content']} | Views: {post['views']}")
                        has_post = True
                if not has_post:
                    print("Has no posts")
        elif choice in ('5', "find user's post"):
            print("-----Authors------")
            for author in users:
                print(author)
            selected_author = input("Which user you want to find?: ")
            print(f"\n----- {selected_author} -----")
            has_post = False
            for post in posts:
                if post['author'] == selected_author:
                    post_views(posts, post['id'], current_user)
                    print(f"{selected_author}: {post['content']} | Views: {post['views']}")
                    has_post = True
            if not has_post:
                print("Has no posts")
        elif choice in ('6', 'show user'):
            print("-----Authors------")
            for author in users:
                print(author)
            author= input("Which user you want to find?: ")
            show_user(posts, users, author, current_user)
        elif choice in ('7', 'exit'): 
            break

main() 