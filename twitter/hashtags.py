# first install library
#pip install python-twitter
#1 sign up for twitter
#2 Go to https://apps.twitter.com/
#3 Create an App
#4 Should be able toi use http://www.marymount.edu for webpage if you do not have one
#5 once created go to Keys and Access tokens
#6 Generate Access Token
#7 use this data for the fields below
#get credentials
import twitter
#fill these in
api = twitter.Api(consumer_key='',
					  consumer_secret='',
					  access_token_key='',
					  access_token_secret='',
				  tweet_mode='extended')





def get_tweets(handle,since_id=0,max_id=0,count=200):
	if max_id == 0:
		statuses = api.GetUserTimeline(screen_name=handle, count=count, exclude_replies=True, include_rts=False,since_id=since_id)
	else:
		statuses = api.GetUserTimeline(screen_name=handle, count=count, exclude_replies=True, include_rts=False,max_id=max_id)
	return statuses


#Fill in Twitter Handle
statuses=get_tweets(handle='', count=500)

TagList={}
count=0
for s in statuses:
	#print(s.full_text)
	hashtags=s.hashtags
	for tag in hashtags:
		if tag.text in TagList.keys():
			TagList[tag.text]+=1
		else:
			TagList[tag.text]=1
	count+=1
	#uncomment to see all things you can gather
	#print(s)
print(TagList)
print(count)
