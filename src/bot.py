# -*- coding: UTF-8 -*-
from fbchat.models import *
from fbchat import Client
from src import chat
from src import weather
import time


class moifb(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        # self.changeNickname(
        #     message_object.text, author_id, thread_id=thread_id, thread_type=thread_type
        # )
        # print(thread_id)
        # print(author_id)
        if author_id != thread_id:
            print(author_id)
            print(thread_id)
            self.setTypingStatus(
                TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type
            )

        # log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        if author_id != self.uid:
            if message_object.text:
                if message_object.text == '/Getid' or message_object.text == '/getid':
                    self.send(Message(text=message_object.author),
                              thread_id=thread_id, thread_type=thread_type)

                elif '/thoitiet' in message_object.text:
                    self.send(Message(text=weather.get()),
                              thread_id=thread_id, thread_type=thread_type)
                else:
                    time.sleep(2)
                    responsechat = chat.response(message_object.text)
                    self.send(Message(
                        text=responsechat),
                        thread_id=thread_id,
                        thread_type=thread_type
                    )

# text='\n \n🙂 Tôi là mói moi. \n- Tôi sẽ rep sau khi đi công việc về \n- Nếu xem tử vi gõ /tuvi <tuổi>; ví dụ: /tuvi sửu. \n- Tin nhắn của bạn: {0}'.format(
