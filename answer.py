def detectHashtag(inputs):
    data = []
    for tweet in inputs:
        hashtag = tweet.entities['hashtags']
        for hash in hashtag:
            if hash['text'].lower() == 'testtweet':
                data.append(tweet)
    return data


def interact(inputs, api, FILE_NAME):
    data = detectHashtag(inputs)
    for i in data[::-1]:
        api.update_status("Hello @" + i.user.screen_name + ", this is an automated response to your tweet. ", i.id)
        api.create_favorite(i.id)
        api.retweet(i.id)
        store_last_seen(FILE_NAME, i.id)


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
