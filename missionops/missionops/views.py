from missionops import db
from missionops import app
from flask import render_template, request
from missionops.models import Switch, Config
from PIL import Image
import urllib2
import StringIO


"""
Function resizes the image for goven url
"""
def image_size(url):
    img = urllib2.urlopen('http://scorescience.humboldt.k12.ca.us/fast/teachers/Mars/fulll_Mars.gif').read()
    im = Image.open(StringIO.StringIO(img))
    newy = (im.size[1]/im.size[0])*288
    return newy

"""
View Function for root url
"""
@app.route("/", methods = ('GET', 'POST'))
def home():
    ysize = 0
    #get the config form
    config_form = request.form
    #Set values in database if form is submitted
    if config_form:
        title = config_form['title']
        image_url = config_form['url']
        config_title = Config.query.filter(Config.key=="title").first()
        if config_title:
            config_title.value = title
        
        config_url = Config.query.filter(Config.key=="url").first()
        if config_url:
            config_url.value = image_url
    db.session.commit()
    
    #get the title 
    title = Config.query.filter(Config.key=="title").first()
    if title and  title.value != "":
        title = title.value
    else:
        title = "Mission Ops"

    image_url = Config.query.filter(Config.key=="url").first()
    if image_url and image_url.value != "":
        image_url = image_url.value
    else:
        image_url = "../static/Mars.jpg"
    ysize = image_size(image_url)
    switch_state = Switch.query.first()
    if switch_state:
        switch = switch_state.switch_state
    else:
        switch = False

    return render_template('app.html', switch=switch, title=title, image_url=image_url,
                           ysize=ysize)


@app.route("/config", methods = ('GET', 'POST'))
def config():
    title = Config.query.filter(Config.key=="title").first()
    if title and  title.value != "":
        title = title.value
    else:
        title = "Mission Ops"

    image_url = Config.query.filter(Config.key=="url").first()
    if image_url and image_url.value != "":
        image_url = image_url.value
    else:
        image_url = "../static/Mars.jpg"
        
    return render_template('config.html', title=title, image_url=image_url)
