import plotly.express as px
import pandas as pd

def opportunity_chart():

    df = pd.DataFrame({

        "Product":[
            "ChatGPT",
            "Gemini",
            "Claude",
            "Grok",
            "Perplexity"
        ],

        "Opportunity":[95,92,88,85,84],

        "Risk":[28,35,30,40,25]

    })

    return px.bar(
        df,
        x="Product",
        y=["Opportunity","Risk"],
        barmode="group",
        title="Opportunity vs Risk"
    )

def radar_chart():

    import plotly.graph_objects as go

    categories = [

        "Innovation",
        "Market",
        "Revenue",
        "Scalability",
        "Brand"

    ]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(

        r=[90,95,88,92,90],
        theta=categories,
        fill='toself',
        name="Gemini"

    ))

    return fig