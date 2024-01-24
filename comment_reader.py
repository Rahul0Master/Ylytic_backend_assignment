from flask import Flask, request, jsonify
from datetime import datetime
import requests

app = Flask(__name__)
REST_API_URL='https://app.ylytic.com/ylytic/test'
response = requests.get(REST_API_URL)
comments = response.json().get('comments', [])

# Parse date in the format of "date-month-year" from the route given by users
def parse_date(date_str):
    return datetime.strptime(date_str, "%d-%m-%Y").strftime("%Y-%m-%d")

# Parse the date from the comments given in the REST API URL in the format of "day, date month year hour:minute:second timezone"
def date_parser(date_str):
    return datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z").strftime("%Y-%m-%d")

@app.route('/search', methods=['GET'])
def search_comments():
    if not comments:
        return jsonify({"error": "Failed to fetch or filter comments"}), 500
    search_author = request.args.get('search_author')
    at_from = request.args.get('at_from')
    at_to = request.args.get('at_to')
    like_from = request.args.get('like_from')
    like_to = request.args.get('like_to')
    reply_from = request.args.get('reply_from')
    reply_to = request.args.get('reply_to')
    search_text = request.args.get('seach_text')
    

    
    filtered_comments = []
    for comment in comments:
        comment_date = date_parser(comment['at'])
        at_from_date = parse_date(at_from) if at_from else None
        at_to_date = parse_date(at_to) if at_to else None
        if (not search_author or search_author.lower() in comment['author'].lower()) \
            and \
           (not at_from or comment_date >= at_from_date) \
            and \
           (not at_to or comment_date <= at_to_date) \
            and \
           (not like_from or comment['like'] >= int(like_from)) \
            and \
           (not like_to or comment['like'] <= float(like_to)) \
            and \
           (not reply_from or comment['reply'] >= int(reply_from)) \
            and \
           (not reply_to or comment['reply'] <= float(reply_to)) \
            and \
           (not search_text or search_text.lower() in comment['text'].lower()):
            filtered_comments.append(comment)
        
    
    return jsonify(filtered_comments)

if __name__ == '__main__':
    app.run(debug=True)
