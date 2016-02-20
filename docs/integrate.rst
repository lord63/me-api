.. _integrate:

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

4. Back to me-api, add the douban middleware to your config file::

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

1. Add github middleware to your config file::

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

2. Go to the app you just created, take down the `Client ID` and `Client Secret`.

3. Back to me-api, add the instagram middleware to your config file::

    $ python generate add

then choose instagram and input the data.

4. Go to "http://api.foo.com/instagram/login", authorize your app to get
   the `access_token`.

5. Take down the `access_token` and fill it in our config file.

6. Restart the server, go to "http://api.foo.com/instagram" and have a check.


Keybase
-------

Short Introduction about Keybase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Well, Keybase_ is a website, but it's also an open source command line program.
Let's walk through a terminal example, which illustrates what Keybase does.
All of this can be embedded into other software, written by anyone. [4]_

Integrate Guide
^^^^^^^^^^^^^^^

Let's assume that your api site is "http://api.foo.com", you host keybase on
"/keybase" path.

1. Add keybase middleware to your config file::

    $ python generate add

then choose keybase and follow the prompt.

2. That's all! Restart the server, go to "http://api.foo.com/keybase"
   and have a check.

Medium
------

Short Introduction about Medium
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Medium_ is a blog-publishing platform. The platform has evolved into a hybrid
of non-professional contributions and professional, paid contributions, an
example of social journalism. [5]_

Integrate Guide
^^^^^^^^^^^^^^^

.. admonition:: WARNING

   UPDATED on 2016-02-20: the way to fetch the lastest posts can't work any more,
   please help. Related discussions are at `issue #8`_.

Let's assume that your api site is "http://api.foo.com", you host medium on
"/medium" path.

1. Add medium middleware to your config file::

    $ python generate add

then choose medium and follow the prompt.

2. That's all! Restart the server, go to "http://api.foo.com/medium"
   and have a check.

Stack Overflow
--------------

Short Introduction about Stack Overflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Stack Overflow`_ serves as a platform for users to ask and answer
questions, and, through membership and active participation, to vote
questions and answers up or down and edit questions and answers. The
website features questions and answers on a wide range of topics in
computer programming.  [6]_

Integrate Guide
^^^^^^^^^^^^^^^

Let's assume that your api site is "http://api.foo.com", you host
stack overflow on "/stackoverflow" path.

1. Go to the `Stack Overflow Apps`_ page and create a new app. Make sure that
   the `OAuth Domain` covers "http://api.foo.com/stackoverflow/login/redirict"
   (site + path + '/login/redirect'). In this example, you can set it as
   "api.foo.com".

2. Go to the app you just created, take down the `Client Id`, `Client Secret`
   and `Key`.

3. Back to me-api, add the stack overflow middleware to your config file::

    $ python generate add

then choose stackoverflow and input the data.

4. Go to "http://api.foo.com/stackoverflow/login", authorize your app to get
   the `access_token`.

5. Take down the `access_token` and fill it in our config file.

6. Restart the server, go to "http://api.foo.com/stackoverflow" and have a check.

Twitter
-------

Short Introduction about Twitter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Twitter`_ (/ˈtwɪtər/) is an online social networking service that enables users
to send and read short messages called "tweets".  [7]_

Integrate Guide
^^^^^^^^^^^^^^^

Let's assume that your api site is "http://api.foo.com", you host twitter on
"/twitter" path.

1. Go to the `Twitter Apps`_ page and create a new app.

2. Go to the app you just created, click the 'Keys and Access Tokens' tab, take down
   the `Consumer Key (API Key)`, `Consumer Secret (API Secret)`, `Access Token` and
   `Access Token Secret`.

3. Back to me-api, add the twitter middleware to your config file::

    $ python generate add

then choose twitter and input the data.

4. Restart the server, go to "http://api.foo.com/twitter" and have a check.

.. _Douban: http://www.douban.com/
.. [1] https://en.wikipedia.org/wiki/Douban
.. _`Douban Apps`: http://developers.douban.com/apikey/
.. _Github: https://github.com/
.. [2] https://en.wikipedia.org/wiki/GitHub
.. _Instagram: https://instagram.com/
.. [3] https://en.wikipedia.org/wiki/Instagram
.. _Instagram Clients: https://instagram.com/developer/clients/manage/
.. _Keybase: https://keybase.io/
.. [4] https://keybase.io/
.. _Medium: https://medium.com/
.. [5] https://en.wikipedia.org/wiki/Medium_%28service%29
.. _`issue #8`: https://github.com/lord63/me-api/issues/8
.. _`Stack Overflow`: http://stackoverflow.com/
.. [6] https://en.wikipedia.org/wiki/Stack_Overflow
.. _`Stack Overflow Apps`: http://stackapps.com/apps/oauth/register
.. _`Twitter`: https://twitter.com/
.. [7] https://en.wikipedia.org/wiki/Twitter
.. _`Twitter Apps`: https://apps.twitter.com/
