import yaml
from requests_oauthlib import OAuth1Session


def main():
    with open("../config/tw_config.yaml", "r") as f:
        c = yaml.safe_load(f)

    tw = OAuth1Session(
        c["API_KEY"], c["API_SECRET_KEY"], c["ACCESS_TOKEN"], c["ACCESS_TOKEN_SECRET"]
    )

    API_ENDPOINT = "https://api.twitter.com/1.1/statuses"
    METHOD_URL = "update.json"
    POST_URL = API_ENDPOINT + "/" + METHOD_URL

    post_reply(tw, POST_URL)


def post_reply(tw, url):

    message = (
        "PythonからTwitter APIを使ってリプライ\n"
        + "#python #api #twitter\n"
        + "https://khid.net/2020/03/python-twitter-api-post-tweet/"
    )
    params = {"status": message, "in_reply_to_status_id": "1238738470639525888"}

    res = tw.post(url, params=params)

    if res.status_code == 200:
        print("Success.")
    else:
        print("Failed.")
        print(" - Responce Status Code : {}".format(res.status_code))
        print(" - Error Code : {}".format(res.json()["errors"][0]["code"]))
        print(" - Error Message : {}".format(res.json()["errors"][0]["message"]))
        # {'errors': [{'code': 170, 'message': 'Missing required parameter: status.'}]}


if __name__ == "__main__":
    main()
