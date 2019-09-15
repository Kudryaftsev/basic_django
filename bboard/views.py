from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Bb
from .models import Rubric

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}

    return render(request, 'bboard/index.html', context)
    # template = loader.get_template('bboard/index.html') #   отчитывается от папки templates
    # bbs = Bb.objects.order_by('-published')
    # context = {'bbs': bbs}                              #   контекст шаблона - набор данных,
    #                                                     #   которые должны быть доступны внутри
    #                                                     #   шаблона в виде переменных и с котороми
    #                                                     #   шаблонизатор объединит шаблон 
    # return HttpResponse(template.render(context, request))

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 
               'rubrics': rubrics, 
               'current_rubric': current_rubric}
               
    return render(request, 'bboard/by_rubric.html', context)


