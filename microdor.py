from microdot import Microdot
from microdot import json_response
app = Microdot()

@app.route('/')
async def index(request):
    return 'Hello, world!'
    
@app.route('/Auth', methods=['POST'])
async def index(request):
    return json_response({"R": 200, "D": 51})

app.run()
