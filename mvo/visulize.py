import matplotlib as plt
import plotly.express as px
import seaborn as sns

def cumulative_return_vis(data):
    fig = px.line(data,
                  x=data.index,
                  y=data.columns,
                  title=f'cumulative returns of porfolio stocks between {data.index.min()} and {data.index.max()}'
                  )
    
    fig.update_xaxes(title_text = 'Date')
    fig.update_yaxes(title_text = 'Cumulative Return in %')

    fig.show()


def correlation_heatmap_vis(data):
    port_corr = data.corr()
    sns.heatmap(port_corr)

if __name__ == '__main__':
    pass
