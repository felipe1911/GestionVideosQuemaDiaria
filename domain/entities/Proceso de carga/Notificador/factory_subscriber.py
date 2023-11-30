from smtp_subs import SMTP_subs
from sms_subs import SMS_subs
from ws_subs import WS_subs

from get_id import get_id_new_subscriber

class FactorySubscriber:
   def create_subscriber(publisher,user,type_subscriber):
        id_new_subcriber = user.id
        if type_subscriber == 'email':
            subscriber  = SMTP_subs(id_new_subcriber,user)
        elif type_subscriber == 'sms':
            subscriber  = SMS_subs(id_new_subcriber,user)
        elif type_subscriber == 'ws':
            subscriber = WS_subs(id_new_subcriber,user)

        return subscriber