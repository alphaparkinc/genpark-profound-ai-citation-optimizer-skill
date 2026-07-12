"""
example_usage.py -- Demonstrates ProfoundAICitationOptimizerClient
"""
from client import ProfoundAICitationOptimizerClient

def main():
    client = ProfoundAICitationOptimizerClient()
    result = client.optimize_citations(
        text_copy="Our API router redirects client LLM endpoints efficiently.",
        statistics=["99.99% uptime SLA", "Reduces API costs by 45% on average"]
    )
    print("[Profound AI Citation Optimizer Result]")
    print(result['citation_optimized_text'])

if __name__ == "__main__":
    main()
