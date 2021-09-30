# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:02:51 2021

@author: gonzalez

"""
"""
    Exercise:
        Create a class to contol a power supply (PS) and provide a main 
        function that shows the usage
        
        The PS has 4 outputs each of then can be set to a given level (range 
        from 0 to 15 V or to 48 V). The state of the supply can be also control between 
        ON:1 and OFF:1.
        
        To test the exercise, a model of the comunication with the instrument is 
        provided, see bellow. 
        
        The commands to interact with the instrument are listed in the model
"""
"""
    Power supply iterface model for testing
"""
from ps_driver import PSDriver
class PS_model():
    PS_OUTPUT1_LEVEL = 0
    PS_OUTPUT1_STATE = 0
    PS_OUTPUT2_LEVEL = 0
    PS_OUTPUT2_STATE = 0
    PS_OUTPUT3_LEVEL = 0
    PS_OUTPUT3_STATE = 0
    PS_OUTPUT4_LEVEL = 0
    PS_OUTPUT4_STATE = 0


    def send_cmd(self, commad_string):
        response = ""
        cmd = commad_string.split(" ")[0]
        if (cmd == "output1:state?"):
            response = str(self.PS_OUTPUT1_STATE)
        elif (cmd == "output2:state?"):
            response = str(self.PS_OUTPUT2_STATE)
        elif (cmd == "output3:state?"):
            response = str(self.PS_OUTPUT3_STATE)
        elif (cmd == "output4:state?"):
            response = str(self.PS_OUTPUT4_STATE)
    
        elif (cmd == "output1:voltage_level?"):
            response = str(float(self.PS_OUTPUT1_LEVEL))
        elif (cmd == "output2:voltage_level?"):
            response = str(float(self.PS_OUTPUT2_LEVEL))
        elif (cmd == "output3:voltage_level?"):
            response = str(float(self.PS_OUTPUT3_LEVEL))
        elif (cmd == "output4:voltage_level?"):
            response = str(float(self.PS_OUTPUT4_LEVEL))
    
        elif (cmd == "output1:state"):
            value = int(commad_string.split(" ")[1])
            self.PS_OUTPUT1_STATE = value
        elif (cmd == "output2:state"):
            value = int(commad_string.split(" ")[1])
            self.PS_OUTPUT2_STATE = value
        elif (cmd == "output3:state"):
            value = int(commad_string.split(" ")[1])
            self.PS_OUTPUT3_STATE = value
        elif (cmd == "output4:state"):
            value = int(commad_string.split(" ")[1])
            self.PS_OUTPUT4_STATE = value
    
        elif (cmd == "output1:voltage_level"):
            value = float(commad_string.split(" ")[1])
            self.PS_OUTPUT1_LEVEL = value
        elif (cmd == "output2:voltage_level"):
            value = float(commad_string.split(" ")[1])
            self.PS_OUTPUT2_LEVEL = value
        elif (cmd == "output3:voltage_state"):
            value = float(commad_string.split(" ")[1])
            self.PS_OUTPUT3_LEVEL = value
        elif (cmd == "output4:voltage_state"):
            value = float(commad_string.split(" ")[1])
            self.PS_OUTPUT4_LEVEL = value
    
        elif (cmd == "output1:curr_limit"):
            value = float(commad_string.split(" ")[1])
            self.PS_OUTPUT1_CURR_LIMIT = value
        else:
            raise("Command is not allowed")
    
    
        return response

"""
    Here the class
"""

class PS_driver():
    pass

"""
    Here the main
"""
def main():
    # example how to use the model
    ps = PS_model()
    response = ps.send_cmd("output2:voltage_level?")
    print(response)
    response = ps.send_cmd("output2:voltage_level 1.2")
    response = ps.send_cmd("output2:voltage_level?")
    print(response)
    
    response = ps.send_cmd("output2:state?")
    print(response)
    response = ps.send_cmd("output2:state 1")
    response = ps.send_cmd("output2:state?")
    print(response)
    response = ps.send_cmd("output1:curr_limit 3.2")
    print(response)
    psd = PSDriver(ps)
    print(psd.ps_output2_state)
    print(psd.ps_output1_level)

if __name__ == '__main__':
    main()


