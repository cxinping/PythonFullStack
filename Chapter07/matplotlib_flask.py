import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import os
import base64
from flask import Flask

app = Flask(__name__)

def plotTree():
    x = np.linspace( -1 , 1, 50  )
    y1 = 2 * x + 1
    y2 = x**2 + 1

    fig = plt.figure()
    plt.plot (x,y1)
    return fig

@app.route('/')
def index():
    html = '''
      <html>
          <body>
              <img src="data:image/png;base64,{}" />
          </body>
       <html>
    '''
    fig = plotTree()
    # Encode image to png in base64
    sio = BytesIO()
    fig.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()

    return html.format(data)

if __name__ == '__main__':
    app.run()

