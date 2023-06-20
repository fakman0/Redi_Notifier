import praw
import sqlite3


def create_database():
    db_connection = sqlite3.connect("database.db")
    cursor = db_connection.cursor()

    # Check if table exists
    cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='posts' ''')
    table_exists = cursor.fetchone()

    # Creates a table if it does not exist
    if not table_exists:
        cursor.execute('''CREATE TABLE posts(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT, score INTEGER, url TEXT)''')
        print("Database and table created successfully.")
    else:
        print("Table 'posts' already exists. Skipping table creation.")

    cursor.close()
    db_connection.close()


def crawl_posts(reddit, subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for submission in subreddit.hot(limit=10):
        post = {
            'title': submission.title,
            'content': submission.selftext,
            'score': submission.score,
            'url': submission.url
        }
        posts.append(post)

    return posts

def add_posts_to_database(posts):
    # Open a connection
    db_connection = sqlite3.connect("database.db")
    cursor = db_connection.cursor()

    for post in posts:
        cursor.execute("INSERT INTO posts (title, content, score, url) VALUES (?, ?, ?, ?)", (post['title'], post['content'], post['score'], post['url']))

    
    db_connection.commit()
    print("Posts added to the database.")
    cursor.close()
    db_connection.close()
