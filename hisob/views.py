from django.shortcuts import render
from .forms import ResultForm

def calculate(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            number1 = form.cleaned_data['num1']
            number2 = form.cleaned_data['num2']
            amal = form.cleaned_data['amal']
        if amal == '+':
            result = number1 + number2
            return render(request, 'result.html', {'result': result})
        elif amal == '-':
            result = number1 - number2
            return render(request, 'result.html', {'result': result})
        elif amal == '*':
            result = number1 * number2
            return render(request, 'result.html', {'result': result})
        elif amal == '/':
            result = number1 / number2
            return render(request, 'result.html', {'result': result})
    else:
        form = ResultForm()
    return render(request, 'home.html', {'form': form})
