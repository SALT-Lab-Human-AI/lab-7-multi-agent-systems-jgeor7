#!/usr/bin/env python3
"""
Quick Demo Script - Both AutoGen and CrewAI
============================================

This script demonstrates the basic usage patterns for both frameworks
using the user's original snippets with proper configuration.
"""

import sys
from pathlib import Path

# Add autogen directory to path for config
sys.path.insert(0, str(Path(__file__).parent / "autogen"))

print("=" * 60)
print("MULTI-AGENT FRAMEWORKS QUICK DEMO")
print("=" * 60)

# ============================================================================
# AUTOGEN DEMO
# ============================================================================
print("\n🤖 AutoGen Framework Demo")
print("-" * 30)

try:
    from autogen import ConversableAgent
    from config import Config
    
    # Get the config list (replaces [...] in original snippet)
    config_list = Config.get_config_list()
    
    # Create agents using ConversableAgent (modern AutoGen API)
    assistant = ConversableAgent(
        name="assistant", 
        system_message="You are a helpful AI assistant specializing in travel advice.",
        llm_config={"config_list": config_list, "temperature": 0.7},
        human_input_mode="NEVER"
    )
    
    user_proxy = ConversableAgent(
        name="user_proxy", 
        system_message="You are a user proxy that initiates conversations.",
        llm_config={"config_list": config_list, "temperature": 0.7}, 
        human_input_mode="NEVER"
    )
    
    # Initiate chat (user's original pattern)
    print("Starting AutoGen conversation...")
    result = user_proxy.initiate_chat(
        assistant, 
        message="Provide 3 quick tips for booking affordable flights to Iceland",
        max_turns=2
    )
    
    print("✅ AutoGen demo completed successfully!")
    
except Exception as e:
    print(f"❌ AutoGen demo failed: {e}")

# ============================================================================
# CREWAI DEMO  
# ============================================================================
print("\n🚀 CrewAI Framework Demo")
print("-" * 30)

try:
    from crewai import Agent, Task, Crew
    
    # Create agent (user's pattern)
    flight_agent = Agent(
        role="Flight Specialist",
        goal="Find the best flights for the trip", 
        backstory="You have booked thousands of flights and know the best times to fly.",
        verbose=False,  # Keep output concise for demo
        allow_delegation=False
    )
    
    # Create task (user's pattern) 
    task = Task(
        description="Research flights from NYC to Reykjavik and provide 3 quick booking tips",
        agent=flight_agent,
        expected_output="List of flight options with prices and booking tips"
    )
    
    # Create crew (user's pattern)
    crew = Crew(
        agents=[flight_agent], 
        tasks=[task], 
        verbose=False,  # Keep output concise for demo
        process="sequential"
    )
    
    print("Starting CrewAI crew execution...")
    result = crew.kickoff()
    
    print("✅ CrewAI demo completed successfully!")
    print("Result:", str(result)[:200] + "..." if len(str(result)) > 200 else str(result))
    
except Exception as e:
    print(f"❌ CrewAI demo failed: {e}")

print(f"\n{'='*60}")
print("Demo completed! Both frameworks are working.")
print("Run the full demos with:")
print("  python autogen/autogen_simple_demo.py")  
print("  python crewai/crewai_demo.py")
print("=" * 60)