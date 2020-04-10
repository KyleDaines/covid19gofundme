from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import stripe

from api.models import Campaign
from api.serializer import CampaignSerializer
# Create your views here.
class CampaignList(APIView):
    #Get all categories or create a category
    @csrf_exempt
    def get(self, request, format=None):
        camp = Campaign.objects.all()
        if request.query_params.get('campaign_id'):
            camp = Campaign.filter(campaign_id__contains=request.query_params.get('campaign_id'))
        serializer = CampaignSerializer(camp, many=True)
        return Response(serializer.data)

class CampaignDetail(APIView):
    #Work with an individual Product object
    @csrf_exempt
    def get(self, request, pk, format=None):
        camp = Campaign.objects.get(campaign_id=pk)
        serializer = CampaignSerializer(camp)
        return Response(serializer.data)

    