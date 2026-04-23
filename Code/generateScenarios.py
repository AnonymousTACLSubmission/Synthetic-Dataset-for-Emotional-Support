
import asyncio
from sotopia.samplers import UniformSampler
from sotopia.server import run_async_server

async def run_multiple_servers(n):
for i in range(n):
  print(f"Starting server run {i + 1}...")
  await run_async_server(
  model_dict={
  "env": "gpt-4",
  "agent1": "gpt-4o-mini",
  "agent2": "gpt-4o-mini",
  },
  sampler=UniformSampler(),
)
print(f"Finished server run {i + 1}.")

# Run the servers 150 times
asyncio.run(run_multiple_servers(150))
