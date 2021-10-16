from django.shortcuts import render
# from personal.models import Question
from operator import attrgetter

from blog.models import BlogPost
# Create your views here.


# def home_screen_view(request):
# 	context = {}
# 	# context['some_string'] = "this is some string that I'm passing to the view"

# 	# context = {
# 	# 	'some_string': "this is some string that I'm passing to the view"
# 	# }

# 	# context['some_number'] = 3151351

# 	# list_of_values = []
# 	# list_of_values.append("first entry")
# 	# list_of_values.append("second entry")
# 	# list_of_values.append("third entry")
# 	# list_of_values.append("fourth entry")
# 	# list_of_values.append("fifth entry")
# 	# context['list_of_values'] = list_of_values


# 	# questions = Question.objects.all()
# 	# context['questions'] = questions

# 	# accounts = Account.objects.all()
# 	# context['accounts'] = accounts    
# 	blog_posts = sorted(BlogPost.objects.all(), key=attrgetter('date_updated'), reverse=True)
# 	context['blog_posts'] = blog_posts
# 	return render(request, "personal/home.html", context)
def home_screen_view(request):
	
	context = {}
	blog_posts = sorted(BlogPost.objects.all(), key=attrgetter('date_updated'), reverse=True)
	context['blog_posts'] = blog_posts

	return render(request, "personal/home.html", context)