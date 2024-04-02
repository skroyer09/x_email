from bottle import get, template, run

######################
@get("/")
def _():
    return "x" 


#######################
run(host="127.0.0.1", port=8080, debug=True, reloader=True)