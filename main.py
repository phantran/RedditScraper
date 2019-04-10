import praw
import csv

# Retrieve data from reddit
reddit = praw.Reddit(client_id="jcgI5y7-kbRM-Q",
                     client_secret="5ohxK2URKeH_wYv8kc8qP1kVpIY",
                     username="phantran197",
                     password="takeonme",
                     user_agent="datascraperv1")


subreddit = reddit.subreddit("python")

hot_python = subreddit.hot(limit=5)


with open("collected_data.csv", 'w') as output_file:
    file_writer = csv.writer(output_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    file_writer.writerow(['CommentID',
                          'Content',
                          'ParentID',
                          'ChildID',
                          'ThreadID',
                          'Subreddit',
                          'UserID',
                          'Upvotes'])

    #file_writer.writerow(['CommentID',
    #                      'Content',
    #                      'ParentID',
    #                      'ChildrenID',
    #                      'ThreadID',
    #                      'Subreddit',
    #                      'UserID'])
    for submission in hot_python:
        if not submission.stickied:
            print(submission.title)
            print("Title: {}, ups: {}, down: {}, Have we visited: {}".format(submission.title,
                                                                                submission.ups,
                                                                                submission.downs,
                                                                                submission.visited))
            #print(submission)
            submission.comments.replace_more(limit=None)
            for comment in submission.comments.list():
                #print(20*'-')
                #print('Parent ID:', comment.parent())
                #print('Comment ID:', comment.id)
                #print(comment.body)
                #print(comment.replies)
                # Save data to csv file
                comment_id = comment.id
                comment_body = comment.body
                parent_id = comment.parent()
                subreddit_id = comment.subreddit_id
                upvotes = comment.score
                author = comment.author
                parent = reddit.comment(comment_id)
                parent.refresh()
                child_comments = parent.replies.list()
                ChildID = ""
                for child_comment_id in child_comments:
                    ChildID = ChildID + child_comment_id.id + ","

                file_writer.writerow([comment_id, comment_body, parent_id, ChildID, submission, subreddit_id, author, upvotes])





