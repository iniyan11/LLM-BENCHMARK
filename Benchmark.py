import ollama
import time
import psutil
import pandas as pd

# models to compare
models = ["phi3", "qwen2.5:3b", "tinyllama"]

# prompts
prompts = [
    "Explain artificial intelligence simply",
    "What is machine learning?",
    "Write a short story about space travel"
]

results = []

print("Benchmark started...\n")

for model in models:
    print(f"\nRunning model: {model}")

    for prompt in prompts:
        print(f"Prompt: {prompt}")

        try:
            start_time = time.time()
            start_mem = psutil.virtual_memory().used

            response = ollama.chat(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )

            end_time = time.time()
            end_mem = psutil.virtual_memory().used

            latency = end_time - start_time
            memory = (end_mem - start_mem) / 1024 / 1024

            answer = response["message"]["content"]

            # quality = word count
            quality = len(answer.split())

            results.append({
                "model": model,
                "prompt": prompt,
                "latency": latency,
                "memory_MB": memory,
                "quality": quality,
                "response": answer
            })

            print("Done\n")

        except Exception as e:
            print("Error:", e)

    # free memory after each model
    try:
        ollama.generate(model=model, prompt="", keep_alive=0)
    except:
        pass

# save results
df = pd.DataFrame(results)
df.to_csv("results.csv", index=False)

print("\nBenchmark completed!")