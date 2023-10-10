from rest_framework.decorators import api_view
from rest_framework.response import Response
from yaml import serialize, serialize_all
from .models import customerDetails
from .serializers import customerDetailsSerializer
from rest_framework import serializers
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/',
		'Search by id': '/?id=<int:pk>',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)




@api_view(['POST'])
def add_customer_with_details(request):
    customerDetails = customerDetailsSerializer(data=request.data)
 
    # validating for already existing data
    # if customerDetails.objects.filter(**request.data).exists():
    #     raise serializers.ValidationError('This data already exists')
 
    if customerDetails.is_valid():
        customerDetails.save()
        return Response(customerDetails.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def view_the_customers_list(request):
     
     
    # checking for the parameters from the URL
    if request.query_params:
        customers = customerDetails.objects.filter(**request.query_params.dict())
    else:
        customers = customerDetails.objects.all()
        # return JsonResponse({'customers': serialize.data})
        # if there is something in items else raise error
    if customers:
        serializer = customerDetailsSerializer(customers, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
# @api_view(['GET'])
# def view_the_customers_list_sort_by_id(request,id):
     
    




@api_view(['POST'])
def update_customer_details(request, pk):
	customers = customerDetails.objects.get(pk=pk)
	data = customerDetailsSerializer(instance=customers, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
     



@api_view(['DELETE'])
def delete_customer_details(request, pk):
	customers = get_object_or_404(customerDetails, pk=pk)
	customers.delete()
	return Response(status=status.HTTP_202_ACCEPTED)



