from langgraph.graph import StateGraph
class State(dict): pass
def build():
    g = StateGraph(State)
    g.add_node("retrieve", lambda s: s)
    g.add_node("answer", lambda s: s)
    g.set_entry_point("retrieve")
    g.add_edge("retrieve", "answer")
    return g.compile()
