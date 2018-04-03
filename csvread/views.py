import json

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd
import os

from theproject import theproject_response
from django.template import RequestContext
import pdb



def index (request):
    request.session['column_names'] = ['Name']
    return render(request, 'csvread/csv_index.html')


class CsvReadFile(APIView):

    def get(self, request):
        """
            Add Project tasks

        """
        print(os.getcwd())
        df_csv = pd.read_csv(os.getcwd() + '/csvread/files/datafile.csv')
        datastore = json.loads(df_csv.to_json(orient='records'))
        gridresponse = {
            'total': len(datastore),
            'records': datastore
        }
        return Response(
           gridresponse,
           status=status.HTTP_200_OK)