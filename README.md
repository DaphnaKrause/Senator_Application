# Senator_Application
This Web Application was created in order to make it easy to find out about your Florida Senators and what bills they have been working on. It was created as a final project for my Advanced Web Apps class.

To begin with I scraped two different websites
1. [A list of current Florida Senators, 2019](https://www.flsenate.gov/Senators/#Senators)
2. [Senators individual sites](https://www.flsenate.gov/Senators/s26)
3. [And the bills they have been working on.](https://www.flsenate.gov/Session/Bills/2019)

I scraped using the following `Jupyter Notebooks`
- FLSenateBills.ipynb
- FLSenatorList.ipynb
- SenatePhotoScrape.ipynb

### From there I set up two different CSV's:
1. senatorList
2. senatebill

Each CSV had a LAST_NAME column, The Last Name of each senator was how I connected the two data sets in my final Flask App.

## On to Flask:
I had to use Jinja2 in-order to feed in my two CSV's

ex.Code Below:
```Jinja2
{% extends 'bootstrap/base.html' %}

{% block content %}
```

The above Jinja2 directives took me a-lot of time to figure out the correct placements.

Within my flask app I installed Bootstrap 4 because I love the clean look behind bootstrap
You do this by importing bootstrap 4 onto your .py page

```HTML
from flask_bootstrap import Bootstrap
```
and then adding the Jinja2 on your additional html pages.

```Jinja2
{% extends 'bootstrap/base.html' %}

{% block content %}
```
Lastly, I had to use `Flask-WTF` for my form on my index.html, It created a drop down menu, including Senators names for the user to choose from.

## Uploading to Reclaim- Python Database:
This is my Adv Web Apps Professor's [instructions for uploading to reclaim hosting](https://docs.google.com/document/d/1W57Pf48E5z1Zg8dsoWrZd1FxkHIqCSrgStXAvqLGQYQ/edit#). I followed it step by step, but ended up having to spend a bit of time on this portion just because I deleted the `passenger_wsgi.py`that it created the first time around.

So my advice would be:
> read carefully and NO DELETING!

## Final Thoughts
All in all the project took me 3-weeks to complete working around 6 hours (probably more) per week.
It was well worth the time because I learned a lot about Flask, Web Scraping, Bootstrap and Reclaim Hosting.
