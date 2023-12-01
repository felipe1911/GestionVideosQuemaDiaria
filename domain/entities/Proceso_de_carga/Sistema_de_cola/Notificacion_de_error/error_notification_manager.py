from .notify_error import notify_error
def error_notification_manager(error_list,videos):
    for i in range(len(error_list)):
        notify_error(error_list[i],videos[i])
        print("")