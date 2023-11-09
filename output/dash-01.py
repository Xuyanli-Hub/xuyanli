import dash  
import dash_core_components as dcc  
import dash_html_components as html  
from dash.dependencies import Input, Output, State  
  
app = dash.Dash(__name__)  
  
app.layout = html.Div([  
    dcc.Input(id='input1', type='number', placeholder='输入第一个数字'),  
    dcc.Input(id='input2', type='number', placeholder='输入第二个数字'),  
    html.Button('求和', id='submit-button'),  
    html.Div(id='result', children='结果将在这里显示')  
])  
  
@app.callback(Output('result', 'children'),  
              [Input('submit-button', 'n_clicks')],  
              [State('input1', 'value'), State('input2', 'value')])  
def update_output(n_clicks, input1, input2):  
    if n_clicks:  
        return f'结果是：{input1 + input2}'  
    else:  
        return ''  
  
if __name__ == '__main__':  
    app.run_server(debug=True)