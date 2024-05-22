from microdot import Microdot

app = Microdot()

@app.route('/')
async def index(request):
    return 'Hello, world!'
    
@app.route('/Auth', methods=['POST'])
async def index(request):
    # Aquí puedes realizar cualquier procesamiento necesario con los datos de la solicitud POST
    # Por ahora, simplemente devolveremos un JSON de ejemplo
    return json_response({"R": 200, "D": 51})

app.run()
