class PID:

    error = 0
    p_error = 0
    I_value = 0

    def __init__(self, P=2.0, I=0.0, D=1.0, Integrator_min=-1, Integrator_max=1):

        self.Kp = P
        self.Ki = I
        self.Kd = D

        self.Integrator_max = Integrator_max
        self.Integrator_min = Integrator_min

    def update(self,reference, measure):
        """
        Calculate PID output value for given reference input and feedback
        """

        self.error = reference - measure
        P_value = self.Kp * self.error
        D_value = self.Kd * (self.error - self.p_error)

        self.I_value += self.Ki * self.error
        self.I_value = min(max(self.I_value, self.Integrator_min),self.Integrator_max)

        PID_value = P_value + self.I_value + D_value
        self.p_error = self.error
        return PID_value


    def setKp(self, P):
        self.Kp = P

    def setKi(self, I):
        self.Ki = I

    def setKd(self, D):
        self.Kd = D