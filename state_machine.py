from enum import Enum

class Motor_State(Enum):
    s0 = 0
    s1 = 1
    s2 = 2
    s3 = 3
    zs1 = 4
    zs2 = 5
    zs3 = 6
    count_error = 7
    fatal_error = 8
    idle = 9
    stop = 10

class Motor_State_Machine:

    def __init__(self):
        self.future_state = Motor_State.idle
        self.previous_state = Motor_State.s0

    def s0(self, a, b, z, start, stop, pause):
        if not stop and not pause:
            if not a and not b and z:
                self.future_state = Motor_State.s0
                #up_down, count_enable, no_error, at_zero
                return False, True, True, False
            elif not a and b and z:
                self.future_state = Motor_State.s1
            elif not a and b and not z:
                self.future_state = Motor_State.zs1
            elif a and not b:
                self.future_state = Motor_State.count_error
            elif a and b:
                self.future_state = Motor_State.fatal_error
        elif stop:
            self.future_state = Motor_State.stop
        elif pause:
            self.future_state = Motor_State.idle
        prevous_state = Motor_State.s0
        #up_down, count_enable, no_error, at_zero
        return False, False, True, False

    def s1(self, a, b, z, start, stop, pause):
        if not stop and not pause:
            if not a and b and z:
                self.future_state = Motor_State.s1
                #up_down, count_enable, no_error, at_zero
                return False, True, True, False
            elif a and b and z:
                self.future_state = Motor_State.s2
            elif not a and not b :
                self.future_state = Motor_State.count_error
            elif a and not b:
                self.future_state = Motor_State.fatal_error
        elif stop:
            self.future_state = Motor_State.stop
        elif pause:
            self.future_state = Motor_State.idle
        self.previous_state = Motor_State.s1
        #up_down, count_enable, no_error, at_zero
        return False, False, True, False

    def s2(self, a, b, z, start, stop, pause):
        if not stop and not pause:
            if a and b and z:
                self.future_state = Motor_State.s2
                #up_down, count_enable, no_error, at_zero
                return False, True, True, False
            elif a and not b and z:
                self.future_state = Motor_State.s3
            elif not a and b:
                self.future_state = Motor_State.count_error
            elif not a and not b:
                self.future_state = Motor_State.fatal_error
        elif stop:
            self.future_state = Motor_State.stop
        elif pause:
            self.future_state = Motor_State.idle
        prevous_state = Motor_State.s2
        #up_down, count_enable, no_error, at_zero
        return False, False, True, False

    def s3(self, a, b, z, start, stop, pause):
        if not stop and not pause:
            if a and not b and z:
                self.future_state = Motor_State.s3
                #up_down, count_enable, no_error, at_zero
                return False, True, True, False
            elif not a and not b and z:
                self.future_state = Motor_State.s0
            elif a and b:
                self.future_state = Motor_State.count_error
            elif not a and b:
                self.future_state = Motor_State.fatal_error
        elif stop:
            self.future_state = Motor_State.stop
        elif pause:
            self.future_state = Motor_State.idle
        self.previous_state = Motor_State.s3
        #up_down, count_enable, no_error, at_zero
        return False, False, True, False

    def zs1(self, a, b, z, start, stop, pause):
        if not stop and not pause:
            if not a and b and not z:
                self.future_state = Motor_State.zs1
                #up_down, count_enable, no_error, at_zero
                return False, True, True, True
            if a and b and not z:
                self.future_state = Motor_State.zs2
            elif not a and not b :
                self.future_state = Motor_State.count_error
            elif a and not b:
                self.future_state = Motor_State.fatal_error
        elif stop:
            self.future_state = Motor_State.stop
        elif pause:
            self.future_state = Motor_State.idle
        self.previous_state = Motor_State.zs1
        #up_down, count_enable, no_error, at_zero
        return False, False, True, True

    def zs2(self, a, b, z, start, stop, pause):
        if not stop and not pause:
            if a and b and not z:
                self.future_state = Motor_State.zs2
                #up_down, count_enable, no_error, at_zero
                return False, True, True, True
            elif a and not b and not z:
                self.future_state = Motor_State.zs3
            elif not a and b:
                self.future_state = Motor_State.count_error
            elif not a and not b:
                self.future_state = Motor_State.fatal_error
        elif stop:
            self.future_state = Motor_State.stop
        elif pause:
            self.future_state = Motor_State.idle
        self.previous_state = Motor_State.zs2
        #up_down, count_enable, no_error, at_zero
        return False, False, True, True

    def zs3(self, a, b, z, start, stop, pause):
        if not stop and not pause:
            if a and not b and not z:
                self.future_state = Motor_State.zs3
                #up_down, count_enable, no_error, at_zero
                return False, True, True, True
            elif not a and not b and not z:
                self.future_state = Motor_State.s0
            elif a and b:
                self.future_state = Motor_State.count_error
            elif not a and b:
                self.future_state = Motor_State.fatal_error
        elif stop:
            self.future_state = Motor_State.stop
        elif pause:
            self.future_state = Motor_State.idle
        self.previous_state = Motor_State.zs3
        #up_down, count_enable, no_error, at_zero
        return False, False, True, True

    def count_error(self, a, b, z, start, stop, pause):
        self.future_state = self.previous_state
        previous = Motor_State.count_error
        #up_down, count_enable, no_error, at_zero
        return True, False, True, False

    def fatal_error(self, a, b, z, start, stop, pause):
        self.future_state = self.previous_state
        previous = Motor_State.fatal_error
        #up_down, count_enable, no_error, at_zero
        return True, False, False, False

    def idle(self, a, b, z, start, stop, pause):
        if start:
            self.future_state = self.previous_state
            previous = Motor_State.idle
            #up_down, count_enable, no_error, at_zero
            return True, True, True, False
        else:
            self.future_state = Motor_State.idle
            #up_down, count_enable, no_error, at_zero
            return True, True, True, False

    def stop(self, a, b, z, start, stop, pause):
        #up_down, count_enable, no_error, at_zero
        return True, True, True, True



    def update(self, current_state, a, b ,z, start, stop ,pause):

        state_functions = { Motor_State.s0: self.s0,
                Motor_State.s1: self.s1,
                Motor_State.s2: self.s2,
                Motor_State.s3: self.s3,
                Motor_State.zs1: self.zs1,
                Motor_State.zs2: self.zs2,
                Motor_State.zs3: self.zs3,
                Motor_State.count_error: self.count_error,
                Motor_State.fatal_error: self.fatal_error,
                Motor_State.idle: self.idle,
                Motor_State.stop: self.stop
                }

        return state_functions[current_state](a, b, z, start, stop, pause)