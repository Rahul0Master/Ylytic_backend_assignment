This Flask web application serves as an API to search and filter comments from given REST API URL. The comments are fetched from a given API endpoint, and the application allows users to perform searches based on various criteria. Here's a short note on the approach of this code:

Fetching Comments:
It uses the requests library to make an HTTP GET request to a specified API endpoint (https://app.ylytic.com/ylytic/test).
The response is then parsed to extract the 'comments' field, representing comments from a YouTube video.

Date Parsing:
The code includes a function (parse_date) to convert date strings from the format '%a, %d %b %Y %H:%M:%S %Z' to '%d %m %Y'. This is used for date comparisons.

Search Parameters:
The application defines a Flask route (/search) to handle search requests via HTTP GET.
It retrieves search parameters such as author name (search_author), date range (at_from and at_to), like and reply count ranges, and search text from the query string.

Filtering Comments:
It iterates through the fetched comments and filters them based on the provided search criteria.
Filters include author name matching, date range matching, like and reply count ranges, and text content matching.

JSON Response:
The filtered comments are then returned as a JSON response to the client.

Error Handling:
The code includes error handling to manage cases where comments cannot be fetched or filtered successfully.

Flask Application:
The application is run in debug mode when executed directly, allowing for easy development and debugging.
This code follows a modular and structured approach, leveraging Flask for creating a simple API that can handle various search criteria to retrieve and filter YouTube video comments dynamically. The goal is to provide flexibility in searching and analyzing comments based on specific user requirements.
This folder contains a python file comment_reader.py

You can access the code on the google colab using the following link:
[Google Colab Link](https://colab.research.google.com/drive/1Z8_M18fbP7lg-rxwWE_sjbCu3zCT_PXG?usp=sharing)
