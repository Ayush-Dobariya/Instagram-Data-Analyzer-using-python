# load the data 

import json

def load_data():
    with open("final_data.json") as data:
        content = json.load(data)
    return content
data = load_data()


def max_posts(data):
    max_posts = 0
    max_user = ""

    for user in data["users"]:
        if user["posts"] > max_posts:
            max_posts = user["posts"]
            max_user = user["name"]

    print(f"{max_user} has the most posts with {max_posts} posts. \n")
max_posts(data)

def max_followers(data):
    max_followers = 0
    max_user = ""

    for user in data["users"]:
        if user["followers"] > max_followers:
            max_followers = user["followers"]
            max_user = user["name"]

    print(f"{max_user} has the most followers with {max_followers} followers. \n")
max_followers(data)

def max_following(data):
    max_following = 0
    max_user = ""

    for user in data["users"]:
        if user["following"] > max_following:
            max_following = user["following"]
            max_user = user["name"]

    print(f"{max_user} has the most following with {max_following} following. \n")
max_following(data)

def category_count(data):
    category_counts = {}

    for user in data["users"]:
        category = user["category"]
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1

    print("Category counts:")
    for category, count in category_counts.items():
        print(f"{category}: {count}")

category_count(data)