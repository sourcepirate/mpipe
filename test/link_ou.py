import context
from mpipe import OrderedStage, UnorderedStage, Pipeline

def increment(value):
    return value + 1

def double(value):
    return value * 2

stage1 = OrderedStage(increment, 3)
stage2 = UnorderedStage(double, 3)
stage1.link(stage2)
pipe = Pipeline(stage1)

for number in range(10):
    pipe.put(number)
pipe.put(None)

for result in pipe.results():
    print(result)
