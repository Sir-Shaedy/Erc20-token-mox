from src.sub_lesson import stateful_fuzz_solv
from hypothesis.stateful import RuleBasedStateMachine, rule
from boa.test.strategies import strategy, settings


class StatefulFuzzer(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.contract = stateful_fuzz_solv.deploy()
        print("Deployed contract!")

    @rule(input=strategy("uint256"))
    def change_number(self, input):
        print(input)
        self.contract.change_number(input)
        print(f"    Called change_number with {input}")

    @rule(input=strategy("uint256"))
    def input_number(self, input):
        response: int = self.contract.always_returns_input_number(input)
        print(f"     Called always_returns with {input}")
        assert response == input, f"Expected {input}, got {response}"


TestStatefulFuzzing = StatefulFuzzer.TestCase
TestStatefulFuzzing.settings = settings(max_examples=1000, stateful_step_count=50)
