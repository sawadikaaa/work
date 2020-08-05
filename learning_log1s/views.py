from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
  return render(request,'learning_log1s/index.html')

def topics(request):
  topics = Topic.objects.order_by('data_added')
  context = {'topics': topics}
  return render(request, 'learning_log1s/topics.html',context)

def topic(request, topic_id):
  topic = Topic.objects.get(id=topic_id)
  entries = topic.entry_set.order_by('-data_added')
  context = {'topic': topic, 'entries': entries}
  return render(request, 'learning_log1s/topic.html',context)