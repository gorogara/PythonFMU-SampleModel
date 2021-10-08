from pythonfmu import Fmi2Causality, Fmi2Slave, Boolean, Integer, Real, String
import math

class Hydro(Fmi2Slave):

    author = "2JAE FATHER"
    description = "Agent for Hydrographic"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.input = ""
        self.output = ""

        self.register_variable(String("input", causality=Fmi2Causality.input))
        self.register_variable(String("output", causality=Fmi2Causality.output))

    def do_step(self, current_time, step_size):

        return True