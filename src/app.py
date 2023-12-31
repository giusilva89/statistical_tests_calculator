import numpy as np
from scipy.stats import t, norm, ttest_ind
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from scipy import stats

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

input_style = {'width': '100%', 'background-color': '#F2F2F2'}
layout_style = {
    'max-width': '800px',
    'margin': '0 auto',
    'background-color': '#EBF4FA',
    'margin-top': '50px',
    'border': '1px solid gray',
    'padding': '20px'
}

button_style = {'height': '50px', 'width': '100%', 'background-color': '#93FFE8', 'color': 'black', 'border': '2px solid #404040'}
button_col_style = {'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}

tr_center_style = {'text-align': 'center', 'vertical-align': 'middle'}

app.layout = dbc.Container(

    [
        dbc.Row(
            dbc.Col(html.H3("T-Test for Comparison of Means", style={'color': '#404040'}), width=12, align='center'),
        ),
        html.Br(),        
        dbc.Row(
            dbc.Col(
                [
                    dbc.Table(
                        [
                            html.Tbody(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.Div("Mean 1", style={'color': '#404040'}),
                                                    dcc.Input(id="mean1-input", type="number", value=0.5, style=input_style),
                                                ],
                                                width=2,
                                                align='center',
                                            ),
                                            dbc.Col(
                                                [
                                                    html.Div("Sample Size 1", style={'color': '#404040'}),
                                                    dcc.Input(id="n1-input", type="number", value=4000, style=input_style),
                                                ],
                                                width=2,
                                                align='center',
                                            ),
                                            dbc.Col(
                                                [
                                                    html.Div("Mean 2", style={'color': '#404040'}),
                                                    dcc.Input(id="mean2-input", type="number", value=0.2, style=input_style),
                                                ],
                                                width=2,
                                                align='center',
                                            ),
                                            dbc.Col(
                                                [
                                                    html.Div("Sample Size 2", style={'color': '#404040'}),
                                                    dcc.Input(id="n2-input", type="number", value=5000, style=input_style),
                                                ],
                                                width=2,
                                                align='center',
                                            ),
                                            dbc.Col(
                                                dbc.Button("T-Test", id="ttest-button1", n_clicks=0, style=button_style, size='lg'),
                                                width=2,
                                                align='center',
                                                style=button_col_style,
                                            ),
                                        ],
                                        style=tr_center_style
                                    ),
                                ]
                            ),
                            html.Tr(id="ttest-results-div1"),
                        ],
                        className="table",
                    ),
                ],
                width=12,
                className="my-4",
            ),
            justify="center",
        ),
        dbc.Row(
            dbc.Col(
                [
                    dbc.Table(
                        [
                            html.Tbody(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.Div("Mean 3", style={'color': '#404040'}),
                                                    dcc.Input(id="mean3-input", type="number", value=0.5, style=input_style),
                                                ],
                                                width=2,
                                                align='center',
                                            ),
                                            dbc.Col(
                                                [
                                                    html.Div("Sample Size 3", style={'color': '#404040'}),
                                                    dcc.Input(id="n3-input", type="number", value=5000, style=input_style),
                                                ],
                                                width=2,
                                                align='center',
                                            ),
                                            dbc.Col(
                                                [
                                                    html.Div("Mean 4", style={'color': '#404040'}),
                                                    dcc.Input(id="mean4-input", type="number", value=0.2, style=input_style),
                                                ],
                                                width=2,
                                                align='center',
                                            ),
                                            dbc.Col(
                                                [
                                                    html.Div("Sample Size 4", style={'color': '#404040'}),
                                                    dcc.Input(id="n4-input", type="number", value=4000, style=input_style),
                                                ],
                                                width=2,
                                                align='center',
                                            ),
                                            dbc.Col(
                                                dbc.Button("T-Test", id="ttest-button2", n_clicks=0, style=button_style, size='lg'),
                                                width=2,
                                                align='center',
                                                style=button_col_style,
                                            ),
                                        ],
                                        style=tr_center_style
                                    ),
                                ]
                            ),
                            html.Tr(id="ttest-results-div2"),
                        ],
                        className="table",
                    ),
                ],
                width=12,
                className="my-4",
            ),
            justify="center",
        ),
        html.Br(),
        html.Br(),          
        dbc.Row(
            dbc.Col(html.H3("Z-Test for Comparison of Proportions", style={'color': '#404040'}), width=12, align='center'),
        ),
        html.Br(),      
        dbc.Row(
            dbc.Col(
                [
                    dbc.Table(
                        [
                            html.Tbody(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.Div("Proportion 1", style={'color': '#404040'}),
                                                    dcc.Input(id="prop1-input", type="number", value=0.69, style=input_style),
                                                ],
                                                width=2,
                                                align='center',
                                            ),
                                            dbc.Col(
                                                [
                                                    html.Div("Sample Size 1", style={'color': '#404040'}),
                                                    dcc.Input(id="n1-prop-input", type="number", value=5000, style=input_style),
                                                ],
                                                width=2,
                                                align='center',
                                            ),
                                            dbc.Col(
                                                [
                                                    html.Div("Proportion 2", style={'color': '#404040'}),
                                                    dcc.Input(id="prop2-input", type="number", value=0.25, style=input_style),
                                                ],
                                                width=2,
                                                align='center',
                                            ),
                                            dbc.Col(
                                                [
                                                    html.Div("Sample Size 2", style={'color': '#404040'}),
                                                    dcc.Input(id="n2-prop-input", type="number", value=4000, style=input_style),
                                                ],
                                                width=2,
                                                align='center',
                                            ),
                                            dbc.Col(
                                                dbc.Button("Z-Test", id="ztest-button1", n_clicks=0, style=button_style, size='lg'),
                                                width=2,
                                                align='center',
                                                style=button_col_style,
                                            ),
                                        ],
                                        style=tr_center_style
                                    ),
                                ]
                            ),
                            html.Tr(id="ztest-results-div1"),
                        ],
                        className="table",
                    ),
                ],
                width=12,
                className="my-4",
            ),
            justify="center",
        ),
        dbc.Row(
            dbc.Col(
                [
                    dbc.Table(
                        [
                            html.Tbody(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.Div("Proportion 3", style={'color': '#404040'}),
                                                    dcc.Input(id="prop3-input", type="number", value=0.32, style=input_style),
                                                ],
                                                width=2,
                                                align='center',
                                            ),
                                            dbc.Col(
                                                [
                                                    html.Div("Sample Size 3", style={'color': '#404040'}),
                                                    dcc.Input(id="n3-prop-input", type="number", value=3100, style=input_style),
                                                ],
                                                width=2,
                                                align='center',
                                            ),
                                            dbc.Col(
                                                [
                                                    html.Div("Proportion 4", style={'color': '#404040'}),
                                                    dcc.Input(id="prop4-input", type="number", value=0.84, style=input_style),
                                                ],
                                                width=2,
                                                align='center',
                                            ),
                                            dbc.Col(
                                                [
                                                    html.Div("Sample Size 4", style={'color': '#404040'}),
                                                    dcc.Input(id="n4-prop-input", type="number", value=1230, style=input_style),
                                                ],
                                                width=2,
                                                align='center',
                                            ),
                                            dbc.Col(
                                                dbc.Button("Z-Test", id="ztest-button2", n_clicks=0, style=button_style, size='lg'),
                                                width=2,
                                                align='center',
                                                style=button_col_style,
                                            ),
                                        ],
                                        style=tr_center_style
                                    ),
                                ]
                            ),
                            html.Tr(id="ztest-results-div2"),
                        ],
                        className="table",
                    ),
                ],
                width=12,
                className="my-4",
            ),
            justify="center",
        ),
    ],
    style=layout_style,
)

def validate_ttest(mean1, n1, mean2, n2, alpha=0.05, n_bootstrap=1000):
    """
    Performs a t-test for two means and a bootstrap test to validate the t-test.

    Args:
        mean1 (float): Mean of the first sample.
        n1 (int): Sample size of the first sample.
        mean2 (float): Mean of the second sample.
        n2 (int): Sample size of the second sample.
        alpha (float, optional): Significance level for the bootstrap test. Default is 0.05.
        n_bootstrap (int, optional): Number of bootstrap iterations. Default is 1000.

    Returns:
        dict: Dictionary containing the results of the tests and calculations.
    """

    # Calculate the standard deviation for each group
    std1 = np.sqrt(mean1 * (1 - mean1) / n1)
    std2 = np.sqrt(mean2 * (1 - mean2) / n2)

    # Calculate the standard error
    se = np.sqrt((std1**2 / n1) + (std2**2 / n2))

    # Calculate the confidence interval for the t-test
    margin_of_error = stats.t.ppf(1 - alpha / 2, n1 + n2 - 2) * se
    confidence_interval_ttest = (mean1 - mean2 - margin_of_error, mean1 - mean2 + margin_of_error)

    # Calculate the test statistic
    test_stat = (mean1 - mean2) / se

    # Calculate the p-value for the t-test
    p_value_ttest = 2 * (1 - stats.t.cdf(abs(test_stat), n1 + n2 - 2))

    # Perform the bootstrap test
    mean_diff = mean1 - mean2
    combined_data = [mean1] * n1 + [mean2] * n2
    bootstrap_diff = np.zeros(n_bootstrap)
    for i in range(n_bootstrap):
        bootstrap_sample = np.random.choice(combined_data, size=n1 + n2, replace=True)
        bootstrap_diff[i] = np.mean(bootstrap_sample[:n1]) - np.mean(bootstrap_sample[n1:])
    
    # Calculate the confidence interval for the bootstrap test
    bootstrap_ci = np.percentile(bootstrap_diff, [100 * alpha / 2, 100 * (1 - alpha / 2)])

    # Calculate the confidence interval based on the differences of the means
    diff_mean_ci = np.percentile(bootstrap_diff, [100 * (alpha / 2), 100 * (1 - alpha / 2)]) + mean_diff

    # Calculate the bootstrap standard error
    bootstrap_se = np.std(bootstrap_diff)

    # Calculate the p-value for the bootstrap test
    p_value_bootstrap = (np.abs(bootstrap_diff) >= np.abs(mean_diff)).mean()

    # Create a dictionary with the results
    results = {
        "T-Test for Two Means": {
            "T-Statistic": test_stat,
            "P-Value": p_value_ttest,
            "Standard Error": se,
            "Confidence Interval": confidence_interval_ttest,
            "Difference in Means": mean_diff,
            "Bootstrap p-value": p_value_bootstrap,
            "Bootstrap Standard Error": bootstrap_se,
            "Bootstrap Confidence Interval": bootstrap_ci,
            "Difference of Means Confidence Interval": diff_mean_ci
    }}

    # Determine if the t-test is validated based on the bootstrap test
    if p_value_bootstrap < alpha:
        results["Validation"] = "The t-test for two means is validated by the bootstrap test."
    else:
        results["Validation"] = "The t-test for two means is not validated."



    return results

def validate_ztest(prop1, n1, prop2, n2, alpha=0.05, n_bootstrap=1000):
    """
    Performs a z-test for two proportions and a bootstrap test to validate the z-test.

    Args:
        prop1 (float): Proportion of the first sample.
        n1 (int): Sample size of the first sample.
        prop2 (float): Proportion of the second sample.
        n2 (int): Sample size of the second sample.
        alpha (float, optional): Significance level for the bootstrap test. Default is 0.05.
        n_bootstrap (int, optional): Number of bootstrap iterations. Default is 1000.

    Returns:
        dict: Dictionary containing the results of the tests and calculations.
    """
    # Calculate the pooled sample proportion
    prop_pooled = (prop1 * n1 + prop2 * n2) / (n1 + n2) 

    # Calculate the standard errors
    se1 = np.sqrt(prop_pooled * (1 - prop_pooled) / n1)
    se2 = np.sqrt(prop_pooled * (1 - prop_pooled) / n2)

    # Calculate the confidence intervals
    margin_of_error1 = stats.norm.ppf(1 - alpha / 2) * se1
    margin_of_error2 = stats.norm.ppf(1 - alpha / 2) * se2
    
    # Ensure confidence intervals are bounded between 0 and 1
    confidence_interval1 = (max(0, prop1 - margin_of_error1), min(1, prop1 + margin_of_error1))
    confidence_interval2 = (max(0, prop2 - margin_of_error2), min(1, prop2 + margin_of_error2))

    # Calculate the test statistic
    z_score = (prop1 - prop2) / np.sqrt(se1**2 + se2**2)

    # Calculate the p-value
    p_value_ztest = 2 * (1 - stats.norm.cdf(abs(z_score)))

    # Perform the bootstrap test
    prop_diff = prop1 - prop2
    combined_prop = (n1 * prop1 + n2 * prop2) / (n1 + n2)
    combined_data = np.concatenate([np.zeros(n1) + combined_prop, np.zeros(n2) + combined_prop])
    bootstrap_diff = np.zeros(n_bootstrap)
    for i in range(n_bootstrap):
        bootstrap_sample = np.random.choice(combined_data, size=n1 + n2, replace=True)
        bootstrap_diff[i] = np.mean(bootstrap_sample[:n1]) - np.mean(bootstrap_sample[n1:])
    p_value_bootstrap = (np.abs(bootstrap_diff) >= np.abs(prop_diff)).mean()

    # Calculate percentage difference between the proportions
    percentage_diff = np.abs((prop1 - prop2) / ((prop1 + prop2) / 2)) * 100

    # Create a dictionary with the results
    results = {
        "Z-Test for Two Proportions": {
            "Z-Score": z_score,
            "P-Value": p_value_ztest,
            "Standard Error 1": se1,
            "Standard Error 2": se2,
            "Confidence Interval 1": confidence_interval1,
            "Confidence Interval 2": confidence_interval2,
            "Difference in Proportions": prop_diff,
            "Bootstrap p-value": p_value_bootstrap,
            "Bootstrap Standard Error 1": np.std(bootstrap_diff),
            "Percentage Difference": percentage_diff
    }}

    # Determine if the z-test is validated based on the bootstrap test
    if p_value_bootstrap < alpha:
        results["Validation"] = "The z-test for two proportions is validated by the bootstrap test."
    else:
        results["Validation"] = "The z-test for two proportions is not validated."

    return results


@app.callback(
    Output("ttest-results-div1", "children"),
    Input("ttest-button1", "n_clicks"),
    State("mean1-input", "value"),
    State("n1-input", "value"),
    State("mean2-input", "value"),
    State("n2-input", "value"),
)
def display_ttest_results1(n_clicks, mean1, n1, mean2, n2):
    if n_clicks > 0:
        ttest_results = validate_ttest(mean1, n1, mean2, n2, alpha=0.05, n_bootstrap=1000)
        # Create a list of div elements to display the results
        result_items = []
        print("Wu, 2021")
        for key, val in ttest_results["T-Test for Two Means"].items():
            result_items.append(html.Div(f"{key}: {val}"))
         

        return result_items

@app.callback(
    Output("ttest-results-div2", "children"),
    Input("ttest-button2", "n_clicks"),
    State("mean3-input", "value"),
    State("n3-input", "value"),
    State("mean4-input", "value"),
    State("n4-input", "value"),
)
def display_ttest_results2(n_clicks, mean1, n1, mean2, n2):
    if n_clicks > 0:
        ttest_results = validate_ttest(mean1, n1, mean2, n2, alpha=0.05, n_bootstrap=1000)
        print("")
        print("")      
        # Create a list of div elements to display the results
        result_items = []
        for key, val in ttest_results["T-Test for Two Means"].items():
            result_items.append(html.Div(f"{key}: {val}"))
        

        return result_items

@app.callback(
    Output("ztest-results-div1", "children"),
    Input("ztest-button1", "n_clicks"),
    State("prop1-input", "value"),
    State("n1-prop-input", "value"),
    State("prop2-input", "value"),
    State("n2-prop-input", "value"),
)
def display_ztest_results1(n_clicks, prop1, n1, prop2, n2):
    if n_clicks > 0:
        ztest_results = validate_ztest(prop1, n1, prop2, n2, alpha=0.05, n_bootstrap=1000)

        # Create a list of div elements to display the results
        result_items = []
        for key, val in ztest_results["Z-Test for Two Proportions"].items():
            result_items.append(html.Div(f"{key}: {val}"))

        return result_items

@app.callback(
    Output("ztest-results-div2", "children"),
    Input("ztest-button2", "n_clicks"),
    State("prop3-input", "value"),
    State("n3-prop-input", "value"),
    State("prop4-input", "value"),
    State("n4-prop-input", "value"),
)
def display_ztest_results2(n_clicks, prop1, n1, prop2, n2):
    if n_clicks > 0:
        ztest_results = validate_ztest(prop1, n1, prop2, n2, alpha=0.05, n_bootstrap=1000)

        # Create a list of div elements to display the results
        result_items = []
        for key, val in ztest_results["Z-Test for Two Proportions"].items():
            result_items.append(html.Div(f"{key}: {val}"))

        return result_items

if __name__ == "__main__":
    app.run_server(debug=False)
