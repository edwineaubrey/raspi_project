
from flask import Flask, render_template
from gpiozero import LED
from time import sleep

app=Flask(__name__)

blue_led=LED(18)

@app.route('/')
@app.route('/off')
def off():
    blue_led.off()
    return render_template('off.html')

@app.route('/on')
def on():
    while True:
        blue_led.on()
        sleep(1)
        blue_led.off()
        sleep(1)
        return render_template('on.html')


if __name__=='__main__':
    app.run(debug=True)
