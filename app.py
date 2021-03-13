from flask import *
import mouse
from pynput.mouse import Button, Controller


app = Flask('__name__')


@app.route('/configuration')
def configuration():
    mouse.move(0,0,duration=0.2) 
    return str(mouse.get_position())


@app.route('/move',methods=['POST'])
def move():
    command = request.json['command']
    position = mouse.get_position()
    if command=='N':
        mouse.move(position[0],position[1]-20,duration=0.1)
    elif command=='S':
        mouse.move(position[0],position[1]+20,duration=0.1)
    elif command=='E':
        mouse.move(position[0]+20,position[1],duration=0.1)
    elif command=='W':
        mouse.move(position[0]-20,position[1],duration=0.1)
    elif command=='NE':
        mouse.move(position[0]+20,position[1]-20,duration=0.1)
    elif command=='NW':
        mouse.move(position[0]-20,position[1]-20,duration=0.1)
    elif command=='SW':
        mouse.move(position[0]-20,position[1]+20,duration=0.1)
    elif command=='SE':
        mouse.move(position[0]+20,position[1]+20,duration=0.1)

    return 'Done'


@app.route('/click')
def click():
    controller = Controller()
    controller.click(Button.left, 1)
    return 'Clicked'

@app.route('/')
def commander():
    return render_template('joy.html')


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=666)
