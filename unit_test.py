#unit test cases
import StringIO
import sys
import io
from helloworld import printtext

def test_printtext():
    capturedOutput = io.StringIO() 
    sys.stdout = capturedOutput                    
    printtext()                                    
    sys.stdout = sys.__stdout__                    
    print ('Captured', capturedOutput.getvalue())
    gettext = capturedOutput.getvalue()
    date_today = date.today()
    if (gettext.__contains__('date_today')):
      print("Correct Date")
     else:
      break   
      

test_printtext()
