import inspect
import logging

#for logging the error, info, debug, warning , critical msgs on the report we cannot use print statement , we have
#to use logger object
#step1- first import the logging package/class present in the python package

class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]#we are using this as to get the file/method name where from where the logs are made
        logger = logging.getLogger(loggerName)#step2- call the get logger method from the logging class which will create
        #logger object which is object of the logging class
        fileHandler = logging.FileHandler('logfile.log')#step4-from the logging file directly call the filehandler
        #method and pass the logging file path, now capture this in new object filehandler and pass this object as
        #argument in the step3
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")#step5-we should also tell the
        #format of logging for this call the method of formatter directly from the logging class and pass the format as argument
        #and capture it in formatter object
        #step6- now call the setformatter method through the filehandler object and pass the format as argument
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object #step3-now we have to tell where to log and how should
        #be the format
        #for that call the method addhandler through logger object and pass the filehandler object
        #filehandler will have the path of the log file where the logs are to be generated

        #so what is happening is format we captured in formatter and passed to filehandler and then filehandler
        #we passed to addhandler, done connections made

        logger.setLevel(logging.DEBUG)#this sets the log level, ex- if level is set to error then from error and below
        #logs will show , above debug, info and warnings will not show
        #levels are -
        #debug>info>warning>error>critical
        return logger #returning logger object