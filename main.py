from instapy import InstaPy
from instapy import smart_run

insta_username = 'YOUR_USERNAME'
insta_password = 'YOUR_PASSWORD'

session = InstaPy(
    username=insta_username,
    password=insta_password,
    headless_browser=True
)

with smart_run(session):
    # like posts by hashtags
    session.like_by_tags(['web', 'programmer'], amount=100)
    # follows every second user.
    session.do_follow(True, percentage=50)
    # comments on every single picture.
    session.do_comment(True, percentage=100)
    session.set_comments(comments=['Wow This is really excellent',
                                   ' You are doing a great job, have a look at my profiles',
                                   'Glad to see your job :heart_eyes:'])
    # set margin by which the bot should perform actions on profiles
    session.set_relationship_bounds(
        enabled=True, delimit_by_numbers=True, max_followers=2000, min_followers=200, min_following=50)
    # supervisor for quantities of action
    session.set_quota_supervisor(enabled=True, peak_likes_hourly=30,
                                 peak_likes_daily=250, peak_comments_daily=250,
                                 peak_comments_hourly=30, sleep_after=['likes', 'follows'])


session.end()
