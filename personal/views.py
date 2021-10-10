from django.shortcuts import render

# Create your views here.


def home_screen_view(request):
	# print(request.headers)
	context = {}
	# context['some_string'] = "this is some string that I'm passing to the view"
	list_of_values = []
	list_of_values.append("first entry")
	list_of_values.append("second entry")
	list_of_values.append("third entry")
	list_of_values.append("fourth entry")
	list_of_values.append("fifth entry")
	context['list_of_values'] = list_of_values

	return render(request, "personal/home.html", context)