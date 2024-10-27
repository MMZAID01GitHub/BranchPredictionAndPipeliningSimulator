# main.py

import random
from predictors import GsharePredictor, PerceptronPredictor
from pipeline import Pipeline
from metrics import PerformanceMetrics
from traces import realistic_trace_generator

# Initialize predictor, pipeline, and metrics
predictors = [GsharePredictor(history_bits=4), PerceptronPredictor(num_weights=128, history_length=8)]

for branch_predictor in predictors:
    pipeline = Pipeline(branch_predictor)
    metrics = PerformanceMetrics()

    # Use the trace generator to create the instruction trace
    trace_length = 10000
    instruction_trace = realistic_trace_generator(trace_length)

    # Run the simulation using the generator
    for instruction in instruction_trace:
        # Process the instruction as usual
        mispredicted = pipeline.process_cycle(instruction)
        
        if mispredicted is None:
            # Stall cycle, increment only cycle count
            metrics.cycles += 1
        else:
            # Active cycle, update both instructions and cycles
            is_branch = instruction["type"] == "branch"
            metrics.update_metrics(is_branch=is_branch, mispredicted=mispredicted)

    # Output final metrics
    misprediction_rate, ipc = metrics.calculate_metrics()
    print(f"Misprediction Rate: {misprediction_rate:.2f}, IPC: {ipc:.2f}")
