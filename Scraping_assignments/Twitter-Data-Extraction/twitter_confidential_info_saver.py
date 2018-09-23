import json

# create a dictionary to store your twitter credentials
twitter_cred = dict()

#Enter your own consumer_key, consumer_secret, access_key and access_secret
#Replacing the stars ("********")
twitter_cred['CONSUMER_KEY'] = "bfbESrhTRGeZR4lVL2rzJf5Lp"
twitter_cred['CONSUMER_SECRET'] = "bsSRT7seQA2tjqdf2zzhqcg4fAOnhLD09RPvd64XArf74SVvgZ"
twitter_cred['ACCESS_KEY'] = "501383347-WHa5DlZRsDReukkJ2Cb8xQRNIa2QhLYyQudY7ToJ"
twitter_cred['ACCESS_SECRET'] = "VNWZLAqkv6NldIg0O11qOY70dh9jjarwLNkseKHfSF2w1"

#Save the information to a json so that it can be reused in code without exposing
#the secret info to public
with open("twitter_credentials.json", "w") as secret_info:
    json.dump(twitter_cred, secret_info, indent=4, sort_keys=True)
