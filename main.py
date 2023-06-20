import fn_login as login
import fn_database as db
import threading
import keyboard

exit_flag = False
# If the user presses the "esc" key, terminate the program.
def keyboard_listener():
    keyboard.wait('esc')
    global exit_flag
    exit_flag = True
    print("Program terminated.")

# Sign in
reddit = login.login_with_credentials()

# If login failed, try again.
while reddit is None:
    print("Login failed. Please try again.")
    reddit = login.login_with_credentials()

# Crawl posts and add in to database
def crawl_add_post():
    while exit_flag == False:
        # Crawl a posts
        posts = db.crawl_posts(reddit, subreddit)
        # Add posts to database
        db.add_posts_to_database(posts)
        db.time.sleep(30)

# Create a database
db.create_database()
subreddit = input("Enter a subreddit title: ")
#threads
#listener_thread = threading.Thread(target=keyboard_listener)
crawler_thread = threading.Thread(target=crawl_add_post)
#listener_thread.start()
crawler_thread.start()

print("Crawl process started.\nPress the \"ESC\" key to end the process.")

#keyboard_listener_thread.join()
crawler_thread.join()