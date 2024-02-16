import sys

def error_message_details(error, error_detail:sys):
    #this will give that on which file exception has occured and on which line the exception has occured
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] line number[{1}] error message[{2}]".format()
    file_name,exc_tb.tb_lineno,str(error)

    return error_message

class CustomException(Exception):
    def __init__(self,error_message, error_details: sys)
        super().__init__(error_message)
        self.error_messsage=error_message_details(error_message, error_details=error_details)
    
    def __str__(self):
        return self.error_messsage