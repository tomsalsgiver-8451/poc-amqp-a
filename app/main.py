from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from proton.reactor import Container
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.input_model import InputModel
from app.handler import Handler

app = FastAPI(title="PoC AMQP 1.0 Service A",
              description='AMQP 1.0 PoC using FastAPI and Qpid Proton',
              version="0.0.1",
              contact={
                  "name": "84.51",
                  "url": "https://www.8451.com",
                  "email": "tom.salsgiver@8451.com",
              },
              license_info={
                  "name": "Apache 2.0",
                  "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
              })


@app.get('/')
async def root():
    return RedirectResponse(url='/docs')


@app.post(path='/send',
          description='Sends a message to the broker on the poc-b queue',
          responses={202: {"description": "Broker message submitted"}},
          status_code=status.HTTP_202_ACCEPTED)
def send(request: Request, inputModel: InputModel):
    Container(Handler('localhost:5672', 'poc-b', inputModel)).run()
    return JSONResponse(status_code=202, content={"message": "Sent message successfully to broker"})
