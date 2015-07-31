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

1. Go to the `Douban Apps`_ page and create a new app. Make sure that the
`callback uri` equals to "http://api.foo.com/douban/login/redirict"
(site + path + '/login/redirect').

2. Go to the app you just created, take down the `API Key` and `Secret`.

3. Go 'test user' page in you app, add your douban account as a test user.

4. Back to me-api, add the douban middleware to your config file:

    $ python generate add

then choose douban and input the data.

5. Go to "http://api.foo.com/douban/login", authorize your app to get
the `access_token`.

6. Take down the `access_token` and fill it in our config file.

7. Restart the server, go to "http://api.foo.com/douban" and have a check.

Github
------

Short Introduction about Github
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GitHub_ is a web-based Git repository hosting service, which offers all of the
distributed revision control and source code management (SCM) functionality
of Git as well as adding its own features.As of 2015, GitHub reports having
over 9 million users and over 21.1 million repositories, making it the largest
code hoster in the world. [2]_

Integrate Guide
^^^^^^^^^^^^^^^

Let's assume that your api site is "http://api.foo.com", you host github on
"/code" path.

1. Add github middleware to your config file:

    $ python generate add

then choose github and follow the prompt.

2. That's all! Restart the server, go to "http://api.foo.com/code"
and have a check.

Instagram
---------

Short Introduction about Instagram
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Instagram_ is an online mobile photo-sharing, video-sharing and social
networking service that enables its users to take pictures and videos,
and share them on a variety of social networking platforms, such as
Facebook, Twitter, Tumblr and Flickr. [3]_

Integrate Guide
^^^^^^^^^^^^^^^

Let's assume that your api site is "http://api.foo.com", you host instagram
on "/instagram" path.

1. Go to the `Instagram Clients`_ page and create a new client. Make sure that
the `Redirect URI` equals to "http://api.foo.com/instagram/login/redirict"
(site + path + '/login/redirect').

2. Go to the app you just created, take down the `API Key` and `Secret`.

3. Back to me-api, add the instagram middleware to your config file:

    $ python generate add

then choose instagram and input the data.

4. Go to "http://api.foo.com/instagram/login", authorize your app to get
the `access_token`.

5. Take down the `access_token` and fill it in our config file.

6. Restart the server, go to "http://api.foo.com/instagram" and have a check.



.. _Douban: http://www.douban.com/
.. [1] https://en.wikipedia.org/wiki/Douban
.. _`Douban Apps`: http://developers.douban.com/apikey/
.. _Github: https://github.com/
.. [2] https://en.wikipedia.org/wiki/GitHub
.. _Instagram: https://instagram.com/
.. [3] https://en.wikipedia.org/wiki/Instagram
.. _Instagram Clients: https://instagram.com/developer/clients/manage/