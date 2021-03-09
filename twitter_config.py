import streamlit as st
import tweepy


TWITTER_CONSUMER_KEY = 'wGCor848zp2dByIi64tRWVIix'
TWITTER_CONSUMER_SECRET = 'iNENCDLhJJcEnvmZ3vuh9bzott36jW5O1yGpcP6BFnqUV9HOrE'
TWITTER_ACCESS_TOKEN = '191486587-FtnzK7sorG5uif4xmkOkd5y0egAEUKes5t3WJTri'
TWITTER_ACCESS_TOKEN_SECRET = 'wOXfO76KL9LK3xKd9vDiyhkK2YCWI2WjCnenQMf59XI7c'

TWITTER_USERNAMES = [
    'traderstewie',
    'the_chart_life',
    'canuck2usa',
    'sunrisetrader',
    'tmltrader'
]

auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

i = 0
for username in TWITTER_USERNAMES:
    tweets = api.user_timeline(username)
    user = api.get_user(username)
    if i != 0:
        st.write("---------------------------------------------------")
    st.subheader(username)
    st.image(user.profile_image_url)
    i += 1
    for tweet in tweets:
        if '$' in tweet.text:
            words = tweet.text.split(' ')
            for word in words:
                if word.startswith('$') and word[1:].isalpha():
                    symbol = word[1:]
                    st.write(symbol)
                    st.write(tweet.text)
                    url = f'https://finviz.com/chart.ashx?t={symbol}'
                    st.image(url)
                    st.write("---------------------------------------------------")