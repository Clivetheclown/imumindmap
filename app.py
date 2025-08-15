import plotly.graph_objects as go
import networkx as nx
import numpy as np


# Create a graph
G = nx.Graph()

# Central node
central_node = "Benefits of DIY Projects"
G.add_node(central_node, size=50, color='#ADD8E6', group='central')

# Category nodes based on book insights
categories = {
    "Environmental Impact": [
        "Reduces waste through upcycling",
        "Conserves energy with efficient designs",
        "Promotes sustainable material use",
        "Lowers carbon footprint"
    ],
    "Economic Benefits": [
        "Saves money on home repairs",
        "Reduces need for new purchases",
        "Increases property value",
        "Lowers utility costs"
    ],
    "Personal Growth": [
        "Enhances DIY skills",
        "Boosts creativity",
        "Provides sense of accomplishment",
        "Encourages problem-solving"
    ],
    "Community & Lifestyle": [
        "Fosters community collaboration",
        "Promotes sustainable living",
        "Encourages sharing of resources",
        "Builds eco-conscious habits"
    ]
}

# Add category nodes and edges to central node
for cat in categories:
    G.add_node(cat, size=30, color='#90EE90', group='category')
    G.add_edge(central_node, cat)

# Add benefit nodes and edges to categories
for cat, benefits in categories.items():
    for benefit in benefits:
        G.add_node(benefit, size=20, color='#FFFFE0', group='benefit')
        G.add_edge(cat, benefit)

# Position nodes using spring layout
pos = nx.spring_layout(G, seed=42, k=0.5)

# Extract node info
node_x = []
node_y = []
node_text = []
node_size = []
node_color = []
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_text.append(node)
    node_size.append(G.nodes[node]['size'])
    node_color.append(G.nodes[node]['color'])

# Extract edge info
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

# Create plotly figure
fig = go.Figure()

# Add edges
fig.add_trace(go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=1.5, color='gray'),
    hoverinfo='none',
    mode='lines'
))

# Add nodes
fig.add_trace(go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    marker=dict(size=node_size, color=node_color, line=dict(width=1, color='black')),
    text=node_text,
    textposition='middle center',
    textfont=dict(size=10, color='black'),
    hoverinfo='text'
))

# Update layout
fig.update_layout(
    title={
        'text': 'Interactive Bubble Mind Map: Benefits of DIY Projects',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    titlefont=dict(size=20),
    showlegend=False,
    hovermode='closest',
    margin=dict(b=20, l=20, r=20, t=60),
    annotations=[dict(
        text="Source: The Green Home by Sally Beattie",
        showarrow=False,
        xref="paper", yref="paper",
        x=0.0, y=-0.05,
        font=dict(size=10)
    )],
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    width=1000,
    height=700,
    plot_bgcolor='white'
)

# Show the figure
fig.show()