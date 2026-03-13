
from Post import Post

all_posts_archive = []

all_posts_archive.append(Post("Marie", "Good morning!"))
all_posts_archive.append(Post("Joe", "Hello!"))
all_posts_archive.append(Post("Alex", "Nice day today!"))
all_posts_archive.append(Post("Jordan", "I am working on my coding project."))

username = input("Enter your username: ")

# your code here
post1 = Post("Marie", "Good morning!")
print(post1)

post2 = Post("Joe", "Hello!")
print(post2)

post3 = Post("Alex", "Nice day today!")
print(post3)

post4 = Post("Jordan", "I am working on my coding project.")
print(post4)

def handlenewpost(user, archive):
    message = input("Enter your message: ")
    new_post = Post(user, message)
    print("Post created: " + str(new_post))
    archive.append(new_post)

def handledeletepost(user, archive):
    post_id = int(input("Enter the post ID of the post you want to delete: "))
    for post in archive:
        if post.get_post_id() == post_id and post.get_user_name() == user:
            archive.remove(post)
            print("Post deleted.")
            return
    print("Post not found or you do not have permission to delete this post.")

def handleprintposts(user, archive):
    print(f"Posts by {user}:")
    found = False
    for post in archive:
        if post.get_user_name() == user:
            print(f"Post ID: {post.get_post_id()}, Message: {post.message}, Timestamp: {post.timestamp}")
            found = True
    if not found:
        print("You have no posts yet.")

def handlechangeuser(user, archive):
    global username
    username = input("Enter your new username: ")
    print("Your username is now " + str(username) + ".")

def handlequit(user, archive):
    print("Goodbye!")

options= ["new," "remove," "change user," "print," "quit"]
user_input = None
while user_input != "quit":
    user_input = input("What would you like to do? Options: new, remove, change user, print, quit: ")
    if user_input == "new":
        handlenewpost(username, all_posts_archive)
    elif user_input == "remove":
        handledeletepost(username, all_posts_archive)
    elif user_input == "print":
        handleprintposts(username, all_posts_archive)
    elif user_input == "change user":
        handlechangeuser(username, all_posts_archive)
    elif user_input == "quit":
        handlequit(username, all_posts_archive)
    else:       print("Invalid option. Please try again.")



if __name__ == "__main__":
    pass