import os

import pandas as pd
import numpy as np
import netCDF4 as nc
import xarray as xr

import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go


def estatisticas():
    CSV_URL = 'http://queimadas.dgi.inpe.br/queimadas/dados-abertos/download/?utm_campaign=dados-abertos&outputFormat=csv&utm_medium=landing-page&time=24h&utm_content=focos_brasil_ms_24h&id=focos_brasil_ms&utm_source=landing-page'


"""
http://queimadas.dgi.inpe.br/queimadas/dados-abertos/exemplos/

# fig is plotly figure object and graph_div the html code for displaying the graph
graph_div = plotly.offline.plot(fig, auto_open = False, output_type="div")
# pass the div to the template
In the template do:




<script>
var x = document.getElementById("demo");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude +
  "<br>Longitude: " + position.coords.longitude;
}
</script>
"""