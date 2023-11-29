from flask import Flask,request,render_template


application=Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))    

if __name__=="__main__":
    application.debug = True
    application.run()       

