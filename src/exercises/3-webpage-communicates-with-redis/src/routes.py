from os import getenv
from time import sleep
from typing import Tuple, Union
from functools import wraps


from flask import render_template, Blueprint, jsonify
import redis
import redis.exceptions



bp = Blueprint("main", __name__)
cache = redis.Redis(host=getenv("REDIS_HOST", "localhost"))


REDDIT_KEY = "count_reddit"
HACKER_NEWS = "count_hackernews"


def handle_redis_call(func):
    """Makes a couple of retries before giving up a redis call"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        error = None
        for _ in range(5):
            try:
                return func(*args, **kwargs)
            except redis.exceptions.ConnectionError as err:
                error = err
        else:
            raise error
    return wrapper


@handle_redis_call
def get_counter(key: str) -> Tuple[str, str]:

    response: Union[bytes, int] = cache.get(key)

    # Create a new amount if doesn't exist
    if response is None:
        response = cache.incr(key)
    else:
        response = int(response.decode())

    return response


@bp.route("/")
def main():
    count_reddit = get_counter(REDDIT_KEY)
    count_hacker_news = get_counter(HACKER_NEWS)
    return render_template("index.html", count_reddit=count_reddit, count_hacker_news=count_hacker_news)


@handle_redis_call
def increase_counter(key: str) -> Tuple[str, str]:
    return cache.incr(key)


@bp.route('/increment_counter/<site>', methods=['POST'])
def increment_counter(site):
    if site not in ['reddit', 'hacker_news']:
        return jsonify({'error': 'Invalid site'}), 400
    
    counter_key = increase_counter(f'count_{site}')
    new_count = int(counter_key)

    return jsonify({'count': new_count})
