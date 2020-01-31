def detectHashtag(inputs):
    List = []
    for tweet in inputs:
        hashtag = tweet.entities['hashtags']
        for hash in hashtag:
            if hash['text'] == 'TestTweet':
                List.append(tweet.id)
    return List


def retweetHashtag(inputs, api):
    Data = detectHashtag(inputs)
    for d in Data:
        api.retweet(d)


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
