import praw
import random

# This function generates a random "user_agent"
def generate_user_agent():
    browsers = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/85.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/85.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36"
    ]

    user_agent = random.choice(browsers)
    return user_agent

# This function allows the user to log in
def login_with_credentials():
    reddit = None
    # API infos
    client_id = "TEjIi_pmWnlrceu4B6X0vw" # This information is publicly available.
    client_secret = "mE3Y4R1IHIHw6zAYn9xhDzdoJpjMiw" # This information is publicly available.
    user_agent = generate_user_agent()

    # User Creds
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Create a user object
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        username=username,
        password=password
    )

    # Verfy session
    try:
        reddit.user.me()
        print("Login successful. User name:", reddit.user.me().name)
        return reddit
    except:
        print("Login error:")
        return None

# Sign in
reddit = login_with_credentials()
# If login failed, try again.
while reddit is None:
    print("Login failed. Please try again.")
    reddit = login_with_credentials()
