from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

# Open a database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# lists all values
@app.route('/posts', methods=['GET'])
def get_all_posts():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()
    conn.close()
    post_dicts = [dict(post) for post in posts]
    return jsonify(post_dicts)

# Sorts score variables
@app.route('/posts/sorted', methods=['GET'])
def get_sorted_scores():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT score FROM posts ORDER BY score DESC')
    scores = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify(scores)


# Finds the content of the score variable
@app.route('/posts/score/<int:score>', methods=['GET'])
def get_post_by_score(score):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posts WHERE score = ?', (score,))
    post = cursor.fetchone()
    conn.close()
    if post:
        return jsonify(dict(post))
    return jsonify({'message': 'Post not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)