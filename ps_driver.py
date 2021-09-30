from ps_driver_interface import IPSDriver

class PSDriver(IPSDriver):
    def __init__(self, model):
        '''Accepting model class and setting up the ps output values'''

        self.model = model

        #setting up all output values
        self.ps_output1_state = self.model.PS_OUTPUT1_STATE
        self.ps_output2_state = self.model.PS_OUTPUT2_STATE
        self.ps_output3_state = self.model.PS_OUTPUT3_STATE
        self.ps_output4_state = self.model.PS_OUTPUT4_STATE

        self.ps_output1_level = self.model.PS_OUTPUT1_LEVEL
        self.ps_output2_level = self.model.PS_OUTPUT2_LEVEL
        self.ps_output3_level = self.model.PS_OUTPUT3_LEVEL
        self.ps_output4_level = self.model.PS_OUTPUT4_LEVEL

    @property
    def ps_output1_state(self):
        return self.output1_state

    @ps_output1_state.setter
    def ps_output1_state(self, state):
        self.output1_state = state

    @property
    def ps_output2_state(self):
        return self.output2_state

    @ps_output2_state.setter
    def ps_output2_state(self, state):
        self.output2_state = state

    @property
    def ps_output3_state(self):
        return self.output3_state

    @ps_output3_state.setter
    def ps_output3_state(self, state):
        self.output3_state = state

    @property
    def ps_output4_state(self):
        return self.output4_state

    @ps_output4_state.setter
    def ps_output4_state(self, state):
        self.output4_state = state

    @property
    def ps_output1_level(self):
        return self.output1_level

    @ps_output1_level.setter
    def ps_output1_level(self, level):
        self.output1_level = level
        if hasattr(self.model, 'PS_OUTPUT1_CURR_LIMIT'):
            self.output1_level = self.model.PS_OUTPUT1_CURR_LIMIT

    @property
    def ps_output2_level(self):
        return self.output2_level

    @ps_output2_level.setter
    def ps_output2_level(self, level):
        self.output2_level = level
        if hasattr(self.model, 'PS_OUTPUT2_CURR_LIMIT'):
            self.output2_level = self.model.PS_OUTPUT2_CURR_LIMIT

    @property
    def ps_output3_level(self):
        return self.output3_level

    @ps_output3_level.setter
    def ps_output3_level(self, level):
        self.output3_level = level
        if hasattr(self.model, 'PS_OUTPUT3_CURR_LIMIT'):
            self.output3_level = self.model.PS_OUTPUT3_CURR_LIMIT

    @property
    def ps_output4_level(self):
        return self.output4_level
        
    @ps_output4_level.setter
    def ps_output4_level(self, level):
        self.output4_level = level
        if hasattr(self.model, 'PS_OUTPUT4_CURR_LIMIT'):
            self.output4_level = self.model.PS_OUTPUT4_CURR_LIMIT

def main():
    #create a model here
    #dummy_model = PS_model()
    psd = PSDriver(dummy_model) #change it to actual model
    psd.ps_output2_state = 1 # ex - set output state
    print(psd.ps_output2_state)
    print(psd.ps_output1_level)


if __name__ == '__main__':
    main()
