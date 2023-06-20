import fn_login as login
import fn_database as db

# Sign in
reddit = login.login_with_credentials()
# If login failed, try again.
while reddit is None:
    print("Login failed. Please try again.")
    reddit = login.login_with_credentials()

# Create a database

db.create_database()
# Crawl a posts
posts = db.crawl_posts(reddit, input("Enter a subreddit title: "))
# Add posts to database
db.add_posts_to_database(posts)