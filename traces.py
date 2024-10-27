# traces.py

import random

def realistic_trace_generator(length=3000000):
    pc = 0
    generated_count = 0
    
    while generated_count < length:
        # Simulate a loop with a fixed number of iterations
        loop_iterations = 5
        for i in range(loop_iterations):
            yield {"pc": pc, "type": "branch", "taken": True}  # Loop branches are taken
            pc += 4
            generated_count += 1
            if generated_count >= length:
                return

        yield {"pc": pc, "type": "branch", "taken": False}  # Exit loop branch is not taken
        pc += 4
        generated_count += 1
        if generated_count >= length:
            return

        # Simulate conditional branches with a certain probability
        for _ in range(3):  # Add a few conditional branches
            yield {
                "pc": pc, 
                "type": "branch", 
                "taken": random.choices([True, False], weights=[0.7, 0.3])[0]
            }
            pc += 4
            generated_count += 1
            if generated_count >= length:
                return

        # Add some non-branch instructions (ALU, LOAD, STORE)
        for _ in range(10):  # Non-branch instructions
            inst_type = random.choice(["alu", "load", "store"])
            yield {"pc": pc, "type": inst_type, "taken": None}  # Non-branches have no 'taken' status
            pc += 4
            generated_count += 1
            if generated_count >= length:
                return
