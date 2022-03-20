
class ResponseClass(object):
    def __init__(self):
        self.__displayMessage = ''
        self.__displayMessageCode = 0
        self.__displayMessageData = []
        self.__realMessage = ''
        self.__statusCode = 0
        self.__data = []
        self.__exceptionRaised = 0
        self.__newData = []
        self.__oldData = []
        self.__displayPopup = 0

    def get_display_message(self):
        return self.__displayMessage


    def set_display_message(self, value):
        self.__displayMessage = value


    def del_display_message(self):
        del self.__displayMessage

    
    def get_display_popup(self):
        return self.__displayPopup


    def set_display_popup(self, value):
        self.__displayPopup = value


    def del_display_popup(self):
        del self.__displayPopup


    def get_display_message_code(self):
        return self.__displayMessageCode


    def get_display_message_data(self):
        return self.__displayMessageData


    def get_real_message(self):
        return self.__realMessage


    def get_status_code(self):
        return self.__statusCode


    def get_data(self):
        return self.__data


    def get_exception_raised(self):
        return self.__exceptionRaised


    def get_new_data(self):
        return self.__newData


    def get_old_data(self):
        return self.__oldData


    def set_display_message_code(self, value):
        self.__displayMessageCode = value


    def set_display_message_data(self, value):
        self.__displayMessageData = value


    def set_real_message(self, value):
        self.__realMessage = value


    def set_status_code(self, value):
        self.__statusCode = value


    def set_data(self, value):
        self.__data = value


    def set_exception_raised(self, value):
        self.__exceptionRaised = value


    def set_new_data(self, value):
        self.__newData = value


    def set_old_data(self, value):
        self.__oldData = value


    def del_display_message_code(self):
        del self.__displayMessageCode


    def del_display_message_data(self):
        del self.__displayMessageData


    def del_real_message(self):
        del self.__realMessage


    def del_status_code(self):
        del self.__statusCode


    def del_data(self):
        del self.__data


    def del_exception_raised(self):
        del self.__exceptionRaised


    def del_new_data(self):
        del self.__newData


    def del_old_data(self):
        del self.__oldData



    def toJson(self):
        return dict(
                    displayMessage = self.__displayMessage,
                    displayMessageCode = self.__displayMessageCode,
                    displayMessageData = self.__displayMessageData,
                    realMessage = self.__realMessage,
                    statusCode = self.__statusCode,
                    data = self.__data,
                    exceptionRaised = self.__exceptionRaised,
                    newData = self.__newData,
                    oldData = self.__oldData,
                    displayPopup = self.__displayPopup
                    )
    
    displayMessageCode = property(get_display_message_code, set_display_message_code, del_display_message_code, "displayMessageCode's docstring")
    displayMessageData = property(get_display_message_data, set_display_message_data, del_display_message_data, "displayMessageData's docstring")
    realMessage = property(get_real_message, set_real_message, del_real_message, "realMessage's docstring")
    statusCode = property(get_status_code, set_status_code, del_status_code, "statusCode's docstring")
    data = property(get_data, set_data, del_data, "data's docstring")
    exceptionRaised = property(get_exception_raised, set_exception_raised, del_exception_raised, "exceptionRaised's docstring")
    newData = property(get_new_data, set_new_data, del_new_data, "newData's docstring")
    oldData = property(get_old_data, set_old_data, del_old_data, "oldData's docstring")
    displayPopup = property(get_display_popup, set_display_popup, del_display_popup, "displayPopup's docstring")
    displayMessage = property(get_display_message, set_display_message, del_display_message, "displayMessage's docstring")
    