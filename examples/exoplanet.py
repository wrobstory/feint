# -*- coding: utf-8 -*-
"""

Exoplanet Data Example

"""
import pandas as pd
import feint

path = 'data/exoplanet.eu_catalog.csv'

df = pd.read_csv(path)

exochart = feint.Chart(df, x=' mass', y=' radius')
exochart.to_template()

