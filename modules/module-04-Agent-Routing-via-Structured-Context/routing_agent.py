# 🏭 Context Engineering Lab - Module 4: Agent Routing via Structured Context
# Demo: LangGraph-based Dynamic Routing Agent

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langchain_core.messages import BaseMessage
from langchain_core.runnables import RunnableLambda
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from typing_extensions import NotRequired

# Step 1: Define the context schema
type MessageList = Annotated[list[BaseMessage], add_messages]

class RoutingContext(TypedDict):
    messages: MessageList
    intent: NotRequired[str]
    use_case: NotRequired[str]
    flavor_profile: NotRequired[str]
    brand_preference: NotRequired[str]
    agent_to_call: NotRequired[str]
    parameters: NotRequired[dict]

# Step 2: Fake schema parser node (could be LLM + OutputParser)
def schema_parser(state: RoutingContext):
    # Simulate parsing user message into structured context (replace with LLM + prompt + parser)
    return {
        "intent": "recommendation",
        "use_case": "evening",
        "flavor_profile": "mild",
        "brand_preference": "Japanese"
    }

# Step 3: Routing Agent node (LLM decides which agent to call)
def routing_agent(state: RoutingContext):
    # In reality this would be an LLM with prompt + function call
    context = {
        "intent": state.get("intent"),
        "use_case": state.get("use_case"),
        "flavor_profile": state.get("flavor_profile"),
        "brand_preference": state.get("brand_preference")
    }
    # Mock routing logic based on intent
    if context["intent"] == "recommendation":
        return {
            "agent_to_call": "recommendation_agent",
            "parameters": {
                "use_case": context["use_case"],
                "flavor_profile": context["flavor_profile"],
                "brand_preference": context["brand_preference"]
            }
        }
    elif context["intent"] == "origin_info":
        return {
            "agent_to_call": "origin_agent",
            "parameters": {
                "brand_preference": context["brand_preference"]
            }
        }
    elif context["intent"] == "health":
        return {
            "agent_to_call": "health_agent",
            "parameters": {
                "flavor_profile": context["flavor_profile"]
            }
        }
    else:
        return {
            "agent_to_call": "fallback_agent",
            "parameters": {"message": "Sorry, I cannot help with that."}
        }

# Step 4: Define mock agent nodes
def recommendation_agent(state: RoutingContext):
    p = state["parameters"]
    return {
        "messages": [
            f"I recommend a {p['flavor_profile']} flavored matcha from a {p['brand_preference']} brand for your {p['use_case']} moments."
        ]
    }

def origin_agent(state: RoutingContext):
    p = state["parameters"]
    return {
        "messages": [
            f"The brand {p['brand_preference']} has deep cultural roots in Japanese tea ceremonies."
        ]
    }

def health_agent(state: RoutingContext):
    p = state["parameters"]
    return {
        "messages": [
            f"Matcha with a {p['flavor_profile']} profile is often associated with high L-theanine levels and a calming effect."
        ]
    }

def fallback_agent(state: RoutingContext):
    return {"messages": [state["parameters"]["message"]]}

# Step 5: Assemble LangGraph
builder = StateGraph(RoutingContext)

builder.add_node("parse_context", RunnableLambda(schema_parser))
builder.add_node("route_agent", RunnableLambda(routing_agent))
builder.add_node("recommendation_agent", RunnableLambda(recommendation_agent))
builder.add_node("origin_agent", RunnableLambda(origin_agent))
builder.add_node("health_agent", RunnableLambda(health_agent))
builder.add_node("fallback_agent", RunnableLambda(fallback_agent))

# Edge wiring
builder.set_entry_point("parse_context")
builder.add_edge("parse_context", "route_agent")

# Conditional logic based on agent_to_call
builder.add_conditional_edges(
    "route_agent",
    lambda state: state["agent_to_call"],
    {
        "recommendation_agent": "recommendation_agent",
        "origin_agent": "origin_agent",
        "health_agent": "health_agent",
        "fallback_agent": "fallback_agent"
    }
)
builder.add_edge("recommendation_agent", END)
builder.add_edge("origin_agent", END)
builder.add_edge("health_agent", END)
builder.add_edge("fallback_agent", END)

graph = builder.compile()

# Test run
input_state = {
    "messages": [
        {"role": "user", "content": "I want a gentle flavored Japanese matcha to drink in the evening."}
    ]
}

result = graph.invoke(input_state)
print("\nFinal Message:", result["messages"][0])
