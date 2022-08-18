import json
from aio_pika.abc import AbstractIncomingMessage
import asyncio

from backend.Consumer import Consumer
from backend.Producer import Producer
from controller import UserController

async def register(message: AbstractIncomingMessage) -> None:
    user = json.loads(message.body)
    controller = UserController()
    uid = await controller.register(
            firstname=user['firstname'], 
            lastname=user['lastname'])
    user.pop('service', None)
    user['uid'] = uid
    await Producer(service='register-out'
        ).send(message=json.dumps(user).encode('UTF-8'))


async def listen() -> None:
    print(" [*] Waiting for messages. To exit press CTRL+C")
    await Consumer(service='register-in'
    ).listen(callback=register)


if __name__ == '__main__':
    asyncio.run(listen())
