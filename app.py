
#importando bibliotecas e dando LOAD no template
import pandas as pd
import numpy as np

from dash import html, dcc, Dash
from dash.dependencies import Input, Output
import plotly.express as px
from dash.exceptions import PreventUpdate

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from dash_bootstrap_templates import load_figure_template
import dash_bootstrap_components as dbc
from IPython.display import Image, display

load_figure_template("FLATLY")
