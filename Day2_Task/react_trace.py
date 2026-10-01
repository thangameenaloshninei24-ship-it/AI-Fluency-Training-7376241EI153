"""Day 2, Part D: print the agent's real ReAct trace to compare with your paper trace."""
from agent import agent
 
QUESTION = ("Which currency gives more Indian Rupees? USD or KWD "
            )
 
print("QUESTION:", QUESTION, "\n")
print("--- the agent's actions and observations ---")
answer = agent(QUESTION, max_steps=8)
print("\nFINAL ANSWER:", answer)
