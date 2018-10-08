from mattermostdriver import Driver
from secrets import username, password


def get_reactions(client, post_id):
    return driver.client.get('/posts/{}/reactions'.format(post_id))


driver = Driver({
    'url': 'fanype.fanap.plus',
    'login_id': username,
    'password': password,
    'port': 443,
    'debug': False,
    'timeout': 5

})

driver.login()

# ToDo get channel name from user
channel_name = 'rumors'
team_name = 'fanap'
channel = driver.channels.get_channel_by_name_and_team_name(team_name, channel_name)
posts = driver.posts.get_posts_for_channel(channel['id'])
print(posts.keys())
for post_id, post in posts['posts'].items():
    reactions = get_reactions(driver, post_id)        
    print(reactions)
    # posts['posts'][post_id]['reactions'] = reactions
    # print(">>>>>>>>>>>>>>>>>>>>>>>> \n" + client.posts.get_post(post))

