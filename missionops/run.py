from missionops import app, db

#run the application
if __name__ == '__main__':
    # Start app
    app.debug = True

    if 'LISTEN_PORT' in app.config:
        port = app.config['LISTEN_PORT']
    else:
        port = 5000
    print "abc"
    app.run('0.0.0.0', port=port)
