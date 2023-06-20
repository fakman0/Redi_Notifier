import functions as fn

# Sign in
reddit = fn.login_with_credentials()
# If login failed, try again.
while reddit is None:
    print("Login failed. Please try again.")
    reddit = fn.login_with_credentials()
