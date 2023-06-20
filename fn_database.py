import praw
import sqlite3
import time


def create_database():
    db_connection = sqlite3.connect("database.db")
    cursor = db_connection.cursor()

    # Check if table exists
    cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='posts' ''')
    table_exists = cursor.fetchone()

    # Creates a table if it does not exist
    if not table_exists:
        cursor.execute('''CREATE TABLE posts(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT, score INTEGER, url TEXT, subreddit_id TEXT)''')
        print("Database and table created successfully.")
    else:
        print("Table 'posts' already exists. Skipping table creation.")

    cursor.close()
    db_connection.close()


def crawl_posts(reddit, subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for submission in subreddit.new(limit=10):
        post = {
            'title': submission.title,
            'content': submission.selftext,
            'score': submission.score,
            'url': submission.url,
            'subreddit_id': submission.subreddit_id
        }
        posts.append(post)

    return posts

def add_posts_to_database(posts):
    # Open a connection
    db_connection = sqlite3.connect("database.db")
    cursor = db_connection.cursor()

    # Get the subreddit_ids of the last 15 posts in the database
    cursor.execute("SELECT subreddit_id FROM posts ORDER BY id DESC LIMIT 15")
    existing_subreddit_ids = set(row[0] for row in cursor.fetchall())

    for post in posts:
        if post['subreddit_id'] not in existing_subreddit_ids:
            cursor.execute("INSERT INTO posts (title, content, score, url, subreddit_id) VALUES (?, ?, ?, ?, ?)", (post['title'], post['content'], post['score'], post['url'], post['subreddit_id']))

    db_connection.commit()
    print("Posts added to the database.")
    cursor.close()
    db_connection.close()

