import pandas as pd

df_followers = pd.read_json('followers.json',encoding="UTF-8")
df_following = pd.read_json('following.json',encoding="UTF-8")

df_followers = pd.DataFrame(list(df_followers['relationships_followers']))
df_followers = pd.DataFrame(list(df_followers['string_list_data']))
df_followers = pd.DataFrame(list(df_followers[0]))
df_followers = pd.DataFrame(list(df_followers['value']),columns=["Followers_Names"])

df_following = pd.DataFrame(list(df_following['relationships_following']))
df_following = pd.DataFrame(list(df_following['string_list_data']))
df_following = pd.DataFrame(list(df_following[0]))
df_following = pd.DataFrame(list(df_following['value']),columns=["Following_Names"])

for follower in df_followers['Followers_Names']:
    for following in df_following['Following_Names']:
        if follower == following:
            df_followers = df_followers[df_followers.Followers_Names != follower]
            df_following = df_following[df_following.Following_Names != following]
            break
print("People who you don't follow:")
print(df_followers)
print("People who don't follow you")
print(df_following)