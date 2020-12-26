import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "ggplot2"
fig = go.Figure(data=[go.Candlestick(x=daily_data['Date'],
                open=daily_data['Open'],
                high=daily_data['High'],
                low=daily_data['Low'],
                close=daily_data['Close'])])

print("Candlestick chart for "+stock_symbol)
fig.show()
