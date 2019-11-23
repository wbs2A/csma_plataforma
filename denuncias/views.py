from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Denuncia
from .forms import DenunciaForm

import pandas as pd
import plotly.graph_objs as go
import plotly.offline as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


def homepage(request):
    return render(request, 'denuncias/homepage.html')


class CreateDenuncia(CreateView):
    model = Denuncia
    fields = ['observacao', 'conhece_origem', 'contato', 'latitude', 'longitude']

    def form_valid(self, form):
        denuncia = form.save(commit=False)
        if self.request.user.is_authenticated:
            denuncia.user = User.objects.get(pk=self.request.user.id)  # use your own profile here
        else:
            denuncia.user = None
        denuncia.save()
        return HttpResponseRedirect('/denuncias/sucesso')


def contatos(request):
    return render(request, 'denuncias/contatos.html')

def sucesso(request):
    return render(request, 'denuncias/sucesso.html')

def relatorios(request):
    py.init_notebook_mode(connected=True)
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')
    trace = go.Scattergeo(
        locationmode='USA-states',
        lon=df['lon'],
        lat=df['lat'],
        text=df['name'] + '- População: ' + df['pop'].astype(str),
        marker=dict(
            size=df['pop'] / 5000,
            color='#e74c3c',
            line={'width': 0.5,
                  'color': '#2c3e50'},
            sizemode='area')
    )
    data = [trace]
    layout = go.Layout(
        title='<b>População americana em 2014</b>',
        titlefont={'family': 'Arial',
                   'size': 24},
        geo={'scope': 'usa',
             'projection': {'type': 'albers usa'},
             'showland': True,
             'landcolor': '#2ecc71',
             'showlakes': True,
             'lakecolor': '#3498db',
             'subunitwidth': 1,
             'subunitcolor': "rgb(255, 255, 255)"
             })
    fig = go.Figure(data=data, layout=layout)
    graph_div = py.plot(fig, auto_open=False, output_type="div")
    context = {'graph_div': graph_div}

    return render(request,'denuncias/relatorios.html', context=context)