
from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
import json
from Partner_App.forms import EmployeeForm


def EmployeeListView(request):
    response = requests.get('http://127.0.0.1:1400/api/employees/')

    if response.status_code==200:
        try:
            dict_data = json.loads(response.text)
        except ValueError:
            return HttpResponse('Sorry, You are not getting JSON Response')
        else:
            return HttpResponse(dict_data)
    else:
        print(response.status_code)
        return HttpResponse(response.text)

def EmployeeDetailView(request,pk):
    response = requests.get('http://127.0.0.1:1400/api/employees/'+str(pk)+'/')

    if response.status_code==200:
        try:
            return HttpResponse(response,content_type='application/json')
        except ValueError:
            return HttpResponse('Sorry, You are not getting JSON Response')
    else:
        print(response.status_code)
        return HttpResponse(response.text)

def EmployeeDeleteView(request,pk):
    response = requests.delete('http://127.0.0.1:1400/api/employees/'+str(pk)+'/')

    if response.status_code==204:
        json_data = json.dumps({"message" : "Requested resource deleted successfully."})
        return HttpResponse(json_data,content_type='application/json')

    else:
        print(response.status_code)
        json_data = json.dumps({"message": "Requested resource not available to delete."})
        return HttpResponse(json_data, content_type='application/json')

def EmployeeCreateView(request):
    payload = {
        "eno" : 10,
        "ename" : "Sachin",
        "salary" : 10000
    }
    response = requests.post('http://127.0.0.1:1400/api/employees/', data=payload)

    if response.status_code==201:
        json_data = json.dumps({"message": "Requested resource created successfully."})
        return HttpResponse(json_data, content_type='application/json')
    else:
        json_data = json.dumps({"message": "Requested resource not created."})
        return HttpResponse(json_data, content_type='application/json')

def EmployeeUpdateView(request,pk):
    response = requests.get('http://127.0.0.1:1400/api/employees/'+str(pk)+'/')
    if response.status_code==200:
        payload = {
            "eno": 10,
            "ename": "Master Sachin",
            "salary": 15000
        }
        response = requests.put('http://127.0.0.1:1400/api/employees/'+str(pk)+'/',
                                data=payload)

        if response.status_code==200:
            json_data = json.dumps({"message": "Requested resource updated successfully."})
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = json.dumps({"message": "Requested resource not updated successfully."})
            return HttpResponse(json_data, content_type='application/json')
    else:
        json_data = json.dumps({"message": "Requested resource not available to GET."})
        return HttpResponse(json_data, content_type='application/json')



def get_all_employees(request):
    response = requests.get('http://127.0.0.1:1400/api/employees/')

    if response.status_code==200:
        employee_list = json.loads(response.text)
        context = {
            'employee_list' : employee_list
        }
        return render(request, 'get_all_employees.html', context)

    else:
        context = {
            "error" : "Employees data not available to display."
        }
        return render(request, 'get_all_employees.html', context)


def get_single_object(request,pk):
    response = requests.get('http://127.0.0.1:1400/api/employees/'+str(pk)+'/')

    if response.status_code==200:
        context = {
            'employee' : json.loads(response.text)
        }
        return render(request,'employee_detail.html',context)
    else:
        context = {
            'error': 'Requested resource not available to get'
        }
        return render(request, 'employee_detail.html', context)



# def delete_object(request,pk):
#     response = requests.delete('http://127.0.0.1:1400/api/employees/'+str(pk)+'/')
#
#     if response.status_code==204:
#         return redirect('employees')
#         # context = {
#         #     'employee' : 'Record deleted successfully.'
#         # }
#         # return render(request,'employee_delete.html',context)
#     else:
#         context = {
#             'error': 'Requested resource not available to delete'
#         }
#         return render(request, 'employee_delete.html', context)

def delete_object(request,pk):
    if request.method=='POST':
        response = requests.delete('http://127.0.0.1:1400/api/employees/' + str(pk) + '/')

        if response.status_code == 204:
            return redirect('employees')

    else:
        response = requests.get('http://127.0.0.1:1400/api/employees/'+str(pk)+'/')

        if response.status_code==200:
            context = {
                'employee' : json.loads(response.text)
            }
            return render(request,'employee_delete.html', context)
        else:
            context = {
                'error': json.loads(response.text)
            }
            return render(request, 'employee_delete.html', context)






def create_object(request):
    if request.method=='POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            eno = request.POST.get('eno')
            ename = request.POST.get('ename')
            salary = request.POST.get('salary')

            payload = {
                "eno" : eno,
                "ename" : ename,
                "salary" : salary,
            }

            response = requests.post('http://127.0.0.1:1400/api/employees/',data=payload)

            if response.status_code==201:
                return redirect('employees')
                # context = {
                #     'data' : json.loads(response.text)
                # }
                # return render(request,'employee_create.html',context)

            else:
                context = {
                    'error': json.loads(response.text)
                }
                return render(request, 'employee_create.html', context)

        else:
            context = {
                'error' : 'Form is not valid'
            }
            return render(request,'employee_create.html',context)

    else:
        form = EmployeeForm()
        return render(request,'employee_create.html',{'form' : form})


def update_object(request,pk):
    if request.method=='POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            eno = request.POST.get('eno')
            ename = request.POST.get('ename')
            salary = request.POST.get('salary')

            payload = {
                "eno" : eno,
                "ename" : ename,
                "salary" : salary,
            }

            response = requests.put('http://127.0.0.1:1400/api/employees/'+str(pk)+'/',
                                      data=payload)
            if response.status_code==200:
                return redirect('employees')
                # context = {
                #     'updated' : json.loads(response.text)
                # }
                # return render(request,'employee_update.html',context)
            else:
                context = {
                    'error': json.loads(response.text)
                }
                return render(request, 'employee_update.html', context)


        else:
            context ={
                'error' : 'Form data not valid'
            }
            return render(request,'employee_update.html',context)
    else:
        response = requests.get('http://127.0.0.1:1400/api/employees/'+str(pk)+'/')

        if response.status_code==200:
            context = {
                'form' : json.loads(response.text)
            }
            return render(request,'employee_update.html',context)
        else:
            context = {
                'error': json.loads(response.text)
            }
            return render(request, 'employee_update.html', context)




















