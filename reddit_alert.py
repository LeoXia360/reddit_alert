from pushbullet import pushbullet
import time
import praw

pb = pushbullet.Pushbullet("o.ahQSgCMX7BvsOsL3DLSZvj3gV2LXxS3H")
iphone = pb.get_device('iPhone')
reddit = praw.Reddit(client_id='7rXS29Qz5OE_CQ',
					 client_secret='GMFx-Bz8AqWFFQcEtbZ8SCeELHA',
					 user_agent='testscript')
subreddit = reddit.subreddit('watchexchange')
submission_log = []


def main():
	while (True):
		for submission in subreddit.new(limit=10):
			if ((submission not in submission_log) and (('rolex'.lower() in submission.title.lower()) or ('hamilton'.lower() in submission.title.lower()))):
				submission_log.append(submission)
				print(submission.title)
				print(submission.url)
				title = submission.title
				subject =  submission.url
				iphone.push_note(title, subject)
		print "Start : %s" % time.ctime()
		time.sleep( 60 )
		print "End : %s" % time.ctime()

main()