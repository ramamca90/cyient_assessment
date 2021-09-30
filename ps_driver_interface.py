from abc import ABCMeta, abstractmethod
class IPSDriver(metaclass=ABCMeta):
    @property
    @abstractmethod
    def ps_output1_state(self):
        '''Abstract method for getting output1 state'''

    @ps_output1_state.setter
    @abstractmethod
    def ps_output1_state(self):
        '''Abstract method for setting up output1 state'''

    @property
    @abstractmethod
    def ps_output2_state(self):
        '''Abstract method for getting output2 state'''

    @ps_output2_state.setter
    @abstractmethod
    def ps_output2_state(self):
        '''Abstract method setting up output2 state'''

    @property
    @abstractmethod
    def ps_output3_state(self):
        '''Abstract method for getting output3 state'''

    @ps_output3_state.setter
    @abstractmethod
    def ps_output3_state(self):
        '''Abstract method setting up output3 state'''

    @property
    @abstractmethod
    def ps_output4_state(self):
        '''Abstract method for getting output4 state'''

    @ps_output4_state.setter
    @abstractmethod
    def ps_output4_state(self):
        '''Abstract method setting up output4 state'''

    @property
    @abstractmethod
    def ps_output1_level(self):
        '''Abstract method for getting output1 level'''

    @ps_output1_level.setter
    @abstractmethod
    def ps_output1_level(self):
        '''Abstract method setting up output1 level'''

    @property
    @abstractmethod
    def ps_output2_level(self):
        '''Abstract method getting output2 level'''

    @ps_output2_level.setter
    @abstractmethod
    def ps_output2_level(self):
        '''Abstract method setting up output2 level'''

    @property
    @abstractmethod
    def ps_output3_level(self):
        '''Abstract method getting output3 level'''

    @ps_output3_level.setter
    @abstractmethod
    def ps_output3_level(self):
        '''Abstract method setting up output3 level'''

    @property
    @abstractmethod
    def ps_output4_level(self):
        '''Abstract method getting output4 level'''

    @ps_output4_level.setter
    @abstractmethod
    def ps_output4_level(self):
        '''Abstract method setting up output4 level'''