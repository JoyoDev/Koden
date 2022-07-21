from koden.task.state import State, state_transition_map
import unittest


class TestState(unittest.TestCase):

    def test_state_running_valid_transition(self):
        state = State.RUNNING

        assert state in state_transition_map[state]
        assert State.COMPLETED in state_transition_map[state]
        assert State.FAILED in state_transition_map[state]

    def test_state_scheduled_valid_transition(self):
        state = State.SCHEDULED

        assert state in state_transition_map[state]
        assert State.RUNNING in state_transition_map[state]
        assert State.FAILED in state_transition_map[state]

    def test_state_running_invalid_transition(self):
        state = State.RUNNING

        assert State.SCHEDULED not in state_transition_map[state]
        assert State.PENDING not in state_transition_map[state]

    def test_state_scheduled_invalid_transition(self):
        state = State.SCHEDULED

        assert State.COMPLETED not in state_transition_map[state]
        assert State.PENDING not in state_transition_map[state]
