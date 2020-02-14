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
		current_state = Motor_State.idle
		future_state = Motor_State.idle
		previous_state = Motor_State.idle

	def update(current_state, a, b ,z, start, stop ,pause):
		return state_functions[current_state](a, b, z, start, stop, pause)

	def s0(a, b, z, start, stop, pause):
		if not stop and not pause:
			if not a and not b and z:
				future_state = Motor_State.s0
				#up_down, count_enable, no_error, at_zero
				return False, False, True, False
			elif not a and b and z:
				future_state = Motor_State.s1
			elif not a and b and not z:
				future_state = Motor_State.zs1
			elif a and not b:
				future_state = Motor_State.count_error
			elif a and b:
				future_state = Motor_State.fatal_error
		elif stop:
			future_state = Motor_State.stop
		elif pause:
			future_state = Motor_State.idle
		prevous_state = Motor_state.s0
		#up_down, count_enable, no_error, at_zero
		return False, False, True, False

	def s1(a, b, z, start, stop, pause):
		if not stop and not pause:
			if not a and b and z:
				future_state = Motor_State.s1
				#up_down, count_enable, no_error, at_zero
				return False, False, True, False
			elif a and b and z:
				future_state = Motor_State.s2
			elif not a and not b :
				future_state = Motor_State.count_error
			elif a not b:
				future_state = Motor_State.fatal_error
		elif stop:
			future_state = Motor_State.stop
		elif pause:
			future_state = Motor_State.idle
		previous_state = Motor_State.s1
		#up_down, count_enable, no_error, at_zero
		return False, False, True, False

	def s2(a, b, z, start, stop, pause):
		if not stop and not pause:
			if a and b and z:
				future_state = Motor_State.s2
				#up_down, count_enable, no_error, at_zero
				return False, False, True, False
			elif a not b and z:
				future_state = Motor_State.s3
			elif not a and b:
				future_state = Motor_State.count_error
			elif not a not b:
				future_state = Motor_State.fatal_error
		elif stop:
			future_state = Motor_State.stop
		elif pause:
			future_state = Motor_State.idle
		prevous_state = Motor_State.s2
		#up_down, count_enable, no_error, at_zero
		return False, False, True, False

	def s3(a, b, z, start, stop, pause):
		if not stop and not pause:
			if a not b and z:
				future_state = Motor_State.s3
				#up_down, count_enable, no_error, at_zero
                return False, False, True, False
			elif not a and not b and z:
				future_state = Motor_State.s0
			elif a and b:
				future_state = Motor_State.count_error
			elif not a and b:
				future_state = Motor_State.fatal_error
		elif stop:
			future_state = Motor_State.stop
		elif pause:
			future_state = Motor_State.idle
		previous_state = Motor_State.s3
        #up_down, count_enable, no_error, at_zero
		return False, False, True, False

	def zs1(a, b, z, start, stop, pause):
		if not stop and not pause:
			if not a and b and not z:
				future_state = Motor_State.zs1
				#up_down, count_enable, no_error, at_zero
				return False, False, True, True
			if a and b and not z:
				future_state = Motor_State.zs2
			elif not a and not b :
				future_state = Motor_State.count_error
			elif a not b:
				future_state = Motor_State.fatal_error
		elif stop:
			future_state = Motor_State.stop
		elif pause:
			future_state = Motor_State.idle
		previous_state = Motor_State.zs1
		#up_down, count_enable, no_error, at_zero
		return False, False, True, True

	def zs2(a, b, z, start, stop, pause):
		if not stop and not pause:
			if a and b and not z:
				future_state = Motor_State.zs2
				#up_down, count_enable, no_error, at_zero
				return False, False, True, True
			elif a and not b and not z:
				future_state = Motor_State.zs3
			elif not a and b:
				future_state = Motor_State.count_error
			elif not a not b:
				future_state = Motor_State.fatal_error
		elif stop:
			future_state = Motor_State.stop
		elif pause:
			future_state = Motor_State.idle
		previous_state = Motor_State.zs2
		#up_down, count_enable, no_error, at_zero
		return False, False, True, True

	def zs3(a, b, z, start, stop, pause):
		if not stop and not pause:
			if a not b and not z:
				future_state = Motor_State.zs3
				#up_down, count_enable, no_error, at_zero
				return False, False, True, True
			elif not a and not b and not z:
				future_state = Motor_State.s0
            elif a and b:
				future_state = Motor_State.count_error
			elif not a and b:
				future_state = Motor_State.fatal_error
		elif stop:
			future_state = Motor_State.stop
		elif pause:
			future_state = Motor_State.idle
		previous_state = Motor_State.zs3
		#up_down, count_enable, no_error, at_zero
		return False, False, True, True
        
    def count_error(a, b, z, start, stop, pause):
        future_state = previous_state
        previous = Motor_State.count_error
        #up_down, count_enable, no_error, at_zero
		return True, False, True, False
        
    def fatal_error(a, b, z, start, stop, pause):
        future_state = Motor_State.stop
        previous = Motor_State.fatal_error
        #up_down, count_enable, no_error, at_zero
        return True, False, False, False
        
    def idle(a, b, z, start, stop, pause):
        if start:
            future_state = previous_state
            previous = Motor_State.idle
            #up_down, count_enable, no_error, at_zero
            return True, True, True, False
        elif:
            future_state = Motor_State.idle
            #up_down, count_enable, no_error, at_zero
            return True, True, True, False
    
    def stop(a, b, z, start, stop, pause):
        return True, True, True, True

	state_functions = { Motor_State.s0: s0,
				Motor_State.s1: s1,
				Motor_State.s2: s2,
				Motor_State.s3: s3,
				Motor_State.zs1: zs1,
				Motor_State.zs2: zs2,
				Motor_State.zs3: zs3,
				Motor_State.count_error: count_error,
				Motor_State.fatal_error: fatal_error,
				Motor_State.idle: idle,
                Motor_State.stop: stop
				}
