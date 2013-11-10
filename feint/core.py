# -*- coding: utf-8 -*-
"""

Core: The core functionality for Feint to interact with Ruse.js

"""
from __future__ import (print_function, division)
import random
import json
from pkg_resources import resource_string
from string import Template

import pandas as pd

GLMATRIX_SRC = "http://astrojs.s3.amazonaws.com/ruse/examples/lib/gl-matrix.js"
RUSE_SRC = "http://astrojs.s3.amazonaws.com/ruse/dist/ruse.js"

class Chart(object):
    """Top level Feint chart"""

    def __init__(self, data=None, x=None, y=None):
        """Initialize feint chart

        Parameters
        ----------
        data: Pandas DataFrame or Series, default None
        x: string, default None
            DataFrame column for x-axis. For series, defaults to
            data column.
        y: string, default None
            DataFrame column for y-axis. For series, default to
            index.

        Output
        ------
        Binds data to Ruse object
        """
        if not isinstance(data, (pd.DataFrame, pd.Series)):
            raise ValueError(
                "Data must be a Pandas DataFrame or Series"
                )

        if not x:
            self.x = 'index'
        else:
            self.x = x
        if not y:
            if isinstance(data, pd.Series):
                self.y = 'series'
            elif isinstance(data, pd.DataFrame):
                raise ValueError(
                    'DataFrames must include a column name for the y-value'
                    )
        else:
            self.y = y

        if isinstance(data, pd.DataFrame):
            self.ruse_data = pd.concat([data[x], data[y]], axis=1)
            self.ruse_data.rename(columns={x: 'x', y: 'y'})

    def display(self):
        """Display a Feint chart in the IPython notebook"""
        from IPython.core.display import HTML
        from IPython.core.display import Javascript
        from IPython.core.display import display

        id = random.randint(0, 2 ** 16)
        js = """
        require(["{0}"], function(glmatrix) {{
            window.mat4 = glmatrix.mat4;
            window.vec3 = glmatrix.vec3;
            console.log(glmatrix);
            $.getScript('{1}',function(){{
                console.log(ruse)
                var chart_element = $("#vis{2}");
                var r = new ruse(chart_element[0], 800, 500);
                r.plot({3});
            }})
        }});""".format(
            GLMATRIX_SRC, RUSE_SRC, id, self.ruse_data.to_json(orient='records')
            )
        a = HTML(
            '<div id="vis%d" style="height: 500px; width: 800px"></div>' % id)
        b = Javascript(js)
        display(a, b)

    def to_template(self, json_path='ruse.json',
                    html_path='feint_template.html'):
        """Export to simple HTML scaffold

        Parameters
        ----------
        json_path: string, default 'ruse.json'
            Path to write JSON data
        html_path: string, default 'feint_template.html'
            Path to write HTML

        Output
        ------
        JSON with Ruse-compatible data
        HTML scaffold
        """

        template = Template(
                str(resource_string('feint', 'feint_template.html'))
                )
        with open(html_path, 'w') as f:
            f.write(template.substitute(json_path=json_path))

        self.ruse_data.to_json(json_path, orient='records')

class Scatter(Chart):
    """Feint scatterplot"""

    def __init__(self, **kwargs):
        """Create a Feint scatterplot"""

        super(Chart, self).__init__(**kwargs)

        self.type = 'scatter'




