from microdot import Microdot
app = Microdot()

@app.route('/')
async def hello_world(request):
    return 'Hello, world!'
    
@app.route('/Auth', methods=['POST'])
async def authenticate(request):
    return {"R": 200, "D": 51}

app.run()
