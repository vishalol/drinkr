from django.shortcuts import render,redirect
from django.http import HttpResponse
import pickle
import os
import numpy as np
import pandas as pd
from drinkr.settings import BASE_DIR

def index(request):
	data_head = ['Are you a student of IIT Roorkee',
	 'What is the approximate percentage of people do you think are frequent alcohol consumer in your college?',
	 'How do you rate an addicted consumer? one who consumes',
	  'What percentage of alcohol consumers do you think are addicted ?',
	   "In which year do you think a non-drinker has a high chance of trying or getting addicted to alcohol consumption? _Bachelor's_",
	  'What percentage of drinkers do you think are binge drinkers (drink more than 5 units in one sitting) ?',
	   'Enjoy the taste.',
	    'Academic pressure.',
	    'Peer pressure',
	    'Family culture.',
	     'Love affairs.',
	    'Family problems.',
	    'Monetary loss.',
	     'Just for fun.',
	     ' _Campus Groups_',
	      ' _Connect well with seniors/juniors/alumnis_',
	    ' _Breakup/Relationship issues_',
	     ' _Out of curiosity/trying everything at least once_',
	    ' _Asked/Influenced by professors_',
	    'How likely do you think alcohol consumption is injurious to health ?']
	if request.method == "POST":
		data = [[1, 	4, 	1, 	1, 1,	1, 	1, 	5, 	5, 	1, 	2, 5.0, 5, 	5, 	3, 	3, 	3, 	3, 	3, 	5.0]]
		data = [[
			request.POST.get('student',1),
			request.POST.get('frequent',1),
			request.POST.get('frate',1),
			request.POST.get('addict',1),
			request.POST.get('year',1),
			request.POST.get('binge',1),
			request.POST.get('taste',1),
			request.POST.get('acad',1),
			request.POST.get('peer',1),
			request.POST.get('family',1),
			request.POST.get('love',1),
			request.POST.get('problem',1),
			request.POST.get('monetary',1),
			request.POST.get('fun',1),
			request.POST.get('campus',1),
			request.POST.get('seniors',1),
			request.POST.get('breakup',1),
			request.POST.get('curiosity',1),
			request.POST.get('proff',1),
			request.POST.get('hihi',1),
		]]
		data = [[int(i) for i in data[0]]]
		df = pd.DataFrame(np.array(data), columns = data_head)
		file = open(os.path.join(BASE_DIR, 'pima.pickle'), 'rb')
		load_model = pickle.load(file)
		result =load_model.predict(df)
		return render(request,'main/index.html',{'res':True, 'result':"{:.2f}".format(result[0]*100)})
	return render(request,'main/index.html',{})

