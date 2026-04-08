import ollama
import time
import psutil
import pandas as pd

# Create process object to track memory of this script
process = psutil.Process()

# Models to test
models = ["tinyllama", "phi3", "qwen2.5:3b"]

# Prompts for evaluation
prompts = [
    "Explain artificial intelligence simply",
    "What is machine learning?",
    "Write a short story about space travel"
]

# Store results
results = []

print("Benchmark started...\n")

# Loop through each model
for model in models:
    print(f"Running model: {model}")

    # Loop through each prompt
    for prompt in prompts:
        print(f"Prompt: {prompt}")

        try:
            # Record start time
            start_time = time.time()

            # Record memory BEFORE execution (in MB)
            mem_before = process.memory_info().rss / 1024 / 1024

            # Send prompt to model
            response = ollama.chat(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )

            # Record end time
            end_time = time.time()

            # Record memory AFTER execution
            mem_after = process.memory_info().rss / 1024 / 1024

            # Calculate latency
            latency = end_time - start_time

            # Calculate memory usage (fixed)
            memory_used = max(0, mem_after - mem_before)

            # Get model response text
            answer = response["message"]["content"]

            # Simple quality metric (word count)
            quality = len(answer.split())

            # Save result
            results.append({
                "model": model,
                "prompt": prompt,
                "latency": latency,
                "memory_MB": memory_used,
                "quality": quality,
                "response": answer
            })

            print("Done\n")

        except Exception as e:
            print("Error:", e)

    # Free model memory (important for low RAM systems)
    try:
        ollama.generate(model=model, prompt="", keep_alive=0)
    except:
        pass

# Convert results to DataFrame
df = pd.DataFrame(results)

# Save results to CSV
df.to_csv("results.csv", index=False)

print("Benchmark completed successfully!")
