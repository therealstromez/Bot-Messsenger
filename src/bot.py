# -*- coding: UTF-8 -*-
from fbchat.models import *
from fbchat import Client
from src import chat
import time



class moifb(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        if author_id != self.uid:
            print(author_id)
            print(thread_id)
            self.setTypingStatus(
                TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type
            )

        # log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        # print(author_id)
        # print(self.uid)
        if author_id != self.uid:
            if message_object.text:
                if message_object.text == '/Getid' or message_object.text == '/getid':
                    self.send(Message(text=message_object.author),
                              thread_id=thread_id, thread_type=thread_type)
                else:
                    # time.sleep(2)
                    # responsechat = chat.response(message_object.text)
                    # cai nay de react
                    self.reactToMessage(message_object.uid, MessageReaction.LOVE)
                    # cai nay de change nickname
                    # self.changeNickname(message_object.text, message_object.author, thread_id=thread_id, thread_type=thread_type)
                    # self.sendLocalImage(
                    #     "img/test/minh.jpg",
                    #     message=Message(text="This is Minh ielts"),
                    #     thread_id=thread_id,
                    #     thread_type=thread_type,
                    # )
                    responsechat = message_object.text
                    # cai nay de gui tin nhan
                    self.send(Message(
                        text=chat.response(responsechat)),
                        thread_id=thread_id,
                        thread_type=thread_type
                    )

# text='\n \n🙂 Tôi là mói moi. \n- Tôi sẽ rep sau khi đi công việc về \n- Nếu xem tử vi gõ /tuvi <tuổi>; ví dụ: /tuvi sửu. \n- Tin nhắn của bạn: {0}'.format(
