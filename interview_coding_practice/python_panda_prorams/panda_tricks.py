import pandas as pd

df = pd.DataFrame({"City": ["SF", "NY"], "Growth": [0.1, -0.2]})
df.style.bar(subset=["Growth"], align="mid", color=["#5fba7d", "#d65f5f"])