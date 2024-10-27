# Branch Prediction and Pipelining Simulator

This project simulates branch prediction and pipelining behaviors in a simplified CPU pipeline. It models typical real-world instruction flow with a mix of branch and non-branch instructions, allowing for the study of different branch predictors and their impact on pipeline performance.

## Project Overview

### Key Features
- **Branch Prediction**: Implements Gshare and Perceptron predictors to simulate branch prediction accuracy.
- **Pipelining**: Models a 5-stage pipeline (`IF`, `ID`, `EX`, `MEM`, `WB`) with mechanisms for pipeline flushing and stalling on mispredictions.
- **Realistic Instruction Trace Generation**: Uses a generator to produce an instruction trace that includes loops, conditional branches, and non-branch instructions, emulating realistic execution patterns without memory overhead.
- **Performance Metrics**: Calculates metrics such as the **Misprediction Rate** and **IPC (Instructions Per Cycle)** to measure pipeline efficiency.

## Directory Structure

- **main.py**: The main entry point for running the simulation. It initializes predictors, the pipeline, and metrics, and it processes each instruction from the trace.
- **predictors.py**: Contains implementations of the Gshare and Perceptron branch predictors.
- **pipeline.py**: Models a basic 5-stage pipeline with functionality for handling stalls and flushing on branch mispredictions.
- **metrics.py**: Defines `PerformanceMetrics` to calculate and track total cycles, mispredictions, and IPC.
- **traces.py**: Generates a realistic instruction trace using a generator, allowing dynamic trace creation with a mix of branch and non-branch instructions.

## Components

### main.py

The `main.py` file orchestrates the simulation. It:
1. **Initializes** the branch predictor, pipeline, and performance metrics.
2. **Generates** the instruction trace using `realistic_trace_generator` from `traces.py`.
3. **Simulates** each instruction:
   - Processes each cycle through the pipeline.
   - Updates metrics based on mispredictions and stalls.
4. **Outputs** the final misprediction rate and IPC, measuring the performance of the pipeline with the given branch predictor.

### predictors.py

- **GsharePredictor**: A dynamic predictor using the global history register (GHR) XORed with the program counter (PC) to index into a Pattern History Table (PHT) of saturating counters.
- **PerceptronPredictor**: A neural-inspired branch predictor that maintains weights for each perceptron and uses global history to predict based on the dot product of weights and history.

Each predictor has methods for **predicting** branch outcomes and **updating** internal state based on actual outcomes.

### pipeline.py

The `Pipeline` class models a 5-stage pipeline and manages control flow. Key features include:
- **Misprediction Handling**: Flushing the pipeline on mispredictions and inserting stall cycles.
- **Stalling Logic**: Introducing 2-cycle stalls after each mispredicted branch to model realistic pipeline delays.

The pipeline processes each instruction and signals whether it was a mispredicted branch or if the cycle was a stall.

### metrics.py

The `PerformanceMetrics` class calculates performance metrics, including:
- **Total Cycles**: Counts active and stall cycles.
- **Misprediction Rate**: Tracks the percentage of branch instructions mispredicted.
- **IPC (Instructions Per Cycle)**: Calculates the efficiency of instruction throughput relative to total cycles.

### traces.py

The `realistic_trace_generator` function produces a dynamic instruction trace that includes:
- **Loop Patterns**: Loops that repeat for a few iterations, with branches taken until the loop exit.
- **Conditional Branches**: Branches that are biased (e.g., 70% taken) to emulate common control structures.
- **Non-Branch Instructions**: A mix of ALU, LOAD, and STORE operations, representing the variety seen in typical programs.

This generator allows for a memory-efficient way to simulate complex instruction flows.

## Running the Simulation

To run the simulation, execute `main.py`:

```bash
python main.py
```

The output will display the misprediction rate and IPC for each predictor used in the simulation.

### Example Output

```text
Misprediction Rate: 0.45, IPC: 0.76
Misprediction Rate: 0.47, IPC: 0.75
```

## Future Extensions

Potential extensions include:
- Adding more branch predictors
- Experimenting with longer and more complex instruction traces.
- Modeling different pipeline structures to observe predictor performance in various CPU designs.

