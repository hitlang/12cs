#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : LANG
import time
import unittest
import redis

ONE_WEEK_IN_SECONDS = 7 * 86400  # A

VOTE_SCORE = 432


def post_article(conn, user, title, link):
    article_id = str(conn.incr('article:'))

    voted = 'voted:' + article_id

    conn.sadd(voted, user)  # 向集合key中 增加元素

    conn.expire(voted, ONE_WEEK_IN_SECONDS)  # 设置key的生命周期,以秒为单位

    now = time.time()

    article = 'article:' + article_id

    conn.hset(article, 'title', title)
    conn.hset(article, 'link', link)
    conn.hset(article, 'poster', user)
    conn.hset(article, 'time', now)
    conn.hset(article, 'votes', 1)

    conn.zadd('score:', mapping={article: now + VOTE_SCORE})
    conn.zadd('time:', mapping={article: now})

    # conn.zadd('score:', article, now + VOTE_SCORE)
    # conn.zadd('time:', article, now)

    return article_id


class TestRedisConn(unittest.TestCase):

    def setUp(self) -> None:
        self.conn = redis.Redis(db=15)
        print(self.conn)

    def test1(self):
        conn = self.conn
        article_id = post_article(conn, 'username', 'A title', 'http://www.google.com')
        print("新增文章id :", article_id)
        self.assertTrue(article_id)

    def tearDown(self) -> None:
        del self.conn
