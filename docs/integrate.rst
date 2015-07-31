Integrate with your sites
=========================

Douban
------

Short Introduction about Douban
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Douban_ (Chinese: 豆瓣; pinyin: Dòubàn), launched on March 6, 2005, is a
Chinese SNS website allowing registered users to record information and
create content related to film, books, music, and recent events and
activities in Chinese cities. [1]_


Integrate Guide
^^^^^^^^^^^^^^^

Let's assume that your api site is "http://api.foo.com", you host douban on
"/douban" path.

1. Go to the `Douban Apps`_ page and
create a new app. Make sure that the `callback uri` equals to
"http://api.foo.com/douban/login/redirict"(site + path + '/login/redirect').

2. Go to the app you just created, take down the `API Key` and `Secret`.

3. Go 'test user' page in you app, add your douban account as a test user.

4. Back to me-api, add the douban middleware to your config file:

    $ python generate add

then choose douban and input the data.

5. Go to "http://api.foo.com/douban/login", authorize your app to get
the `access_token`.

6. Take down the `access_token` and fill it in our config file.

7. Restart the server, go to "http://api.foo.com/douban" and have a check.


.. _Douban: http://www.douban.com/
.. [1] https://en.wikipedia.org/wiki/Douban
.. _`Douban Apps`: http://developers.douban.com/apikey/