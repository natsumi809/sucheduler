import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task

def index(request):
    todo_list = Task.objects.filter(date__isnull=True)
    calendar_tasks = Task.objects.filter(date__isnull=False)
    return render(request, 'tasks/index.html', {
        'todo_list': todo_list,
        'calendar_tasks': calendar_tasks
    })

@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # end_date を取得するように追加
            Task.objects.create(
                title=data.get('title'),
                date=data.get('date') or None,
                end_date=data.get('end_date') or None, # 追加
                time=data.get('time') or None,
                color=data.get('color', '#007aff')
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def edit_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            task = Task.objects.get(id=data.get('id'))
            task.title = data.get('title')
            task.color = data.get('color')
            task.date = data.get('date') or None
            task.end_date = data.get('end_date') or None # 追加
            task.time = data.get('time') or None
            task.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

# カレンダーでドラッグして期間を変更した時の専用関数
@csrf_exempt
def update_task_duration(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            task = Task.objects.get(id=data.get('id'))
            # FullCalendarのstartStr, endStrを受け取る
            task.date = data.get('start').split('T')[0]
            if data.get('end'):
                task.end_date = data.get('end').split('T')[0]
            else:
                task.end_date = None
            task.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def update_task_date(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task = Task.objects.get(id=data.get('id'))
        new_date = data.get('start').split('T')[0]
        task.date = new_date
        task.save()
        return JsonResponse({'status': 'success'})

@csrf_exempt
def remove_task_date(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task = Task.objects.get(id=data.get('id'))
        task.date = None
        task.save()
        return JsonResponse({'status': 'success'})

@csrf_exempt
def delete_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Task.objects.filter(id=data.get('id')).delete()
        return JsonResponse({'status': 'success'})

@csrf_exempt
def delete_all_todo(request):
    if request.method == 'POST':
        # dateがisnull（空）のタスクのみをフィルタリングして削除
        Task.objects.filter(date__isnull=True).delete()
        return JsonResponse({'status': 'success'})