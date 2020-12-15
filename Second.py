from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def root() -> str:
    return "Welcome to the API"

#printing Dynamic URL! 
#Question though is that the user_id has wrong annotation format
@app.route('/print/<username>/<int:user_id>', methods=['GET'])
def print(username:str, user_id:int):
    return "hello {}, Your ID is {}".format(username, user_id)


if __name__ == "__main__":
    app.run()