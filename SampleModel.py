from pythonfmu import Fmi2Causality, Fmi2Slave, Boolean, Integer, Real, String
import math

class SampleModel(Fmi2Slave):

    author = "JO Gyeongmin"
    description = "Sample Model for python environments"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.intOut = 0
        self.realOut = 0.0
        self.intInput = 0
        self.realInput = 0.0

        self.register_variable(Integer("intOut", causality=Fmi2Causality.output))
        self.register_variable(Real("realOut", causality=Fmi2Causality.output))
        self.register_variable(Integer("intInput", causality=Fmi2Causality.input))
        self.register_variable(Real("realInput", causality=Fmi2Causality.input))

    def do_step(self, current_time, step_size):
        self.intOut = math.sin(current_time) * 100
        self.realOut = math.sin(current_time)

        return True