from django.shortcuts import render

from .models import Calculator

def index(request):

	context = {}

	if(request.method == "POST"):

		try:

			initialcapital = float(request.POST.get('initial'))
			years = float(request.POST.get('years'))
			rate = float(request.POST.get('interest'))
			finalcapital = initialcapital * (1 + ((rate/100)/12))**(12*years)

			if(initialcapital<=0):
				context['error'] = "Please enter a positive number in the 'Initial Capital' field."
			elif (years<=0):
				context['error'] = "Please enter a positive number in the 'Number of Years' field."
			elif (rate<=0):
				context['error'] = "Please enter a positive number in the 'Interest Rate' field."

			else:
				context['initial'] = initialcapital
				context['years'] = years
				context['interest'] = rate
				context['final'] = finalcapital

				c = Calculator(initial_capital = initialcapital, number_of_years = years, interest_rate = rate, final_capital = finalcapital)
				c.save()

		except ValueError:
			context['error'] = "Error! Please enter a value in each field."

	return render(request, "savingscalculator/index.html", context)

def queries(request):

	Queries = Calculator.objects.all()

	context = {'Queries' : Queries}
	
	return render(request, "savingscalculator/queries.html", context)
