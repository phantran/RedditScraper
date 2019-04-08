import praw

# Retrieve data from reddit
reddit = praw.Reddit(client_id="jcgI5y7-kbRM-Q",
                     client_secret="5ohxK2URKeH_wYv8kc8qP1kVpIY",
                     username="phantran197",
                     password="takeonme",
                     user_agent="datascraperv1")


subreddit = reddit.subreddit("python")

hot_python = subreddit.hot(limit=3)

for submission in hot_python:
    if not submission.stickied:
        print(submission.title)
        print("Title: {}, ups: {}, down: {}, Have we visited: {}".format(submission.title,
                                                                         submission.ups,
                                                                         submission.downs,
                                                                         submission.visited))

        submission.comments.replace_more(limit=None)

        for comment in submission.comments.list():
            print(20*'-')
            print('Parent ID:', comment.parent())
            print('Comment ID:', comment.id)
            print(comment.body)
            # Save data to csv file



