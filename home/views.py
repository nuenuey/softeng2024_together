from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render
from django.http import HttpResponse

restaurants = [
    {"id": 1, "name": "돼지박사", "address": "전북 전주시 완산구 전주객사3길 49"},
    {"id": 2, "name": "스시미라이", "address": "전북 전주시 완산구 충경로 29"},
    {"id": 3, "name": "큰집피순대", "address": "전북 전주시 덕진구 덕용4길 4"},
    {"id": 4, "name": "또순이네집", "address": "전북 전주시 완산구 전주객사3길 11-8"},
    {"id": 5, "name": "온담", "address": "전북 전주시 완산구 전주천동로 210 1층"},
    {"id": 6, "name": "연지본관", "address": "전북 전주시 완산구 현무1길 15"},
    {"id": 7, "name": "전주초장집", "address": "전북 전주시 완산구 전주객사2길 45-10 1층"},
    {"id": 8, "name": "전주 수정관", "address": "전북 전주시 완산구 문화광장로 18"},
    {"id": 9, "name": "돈카츠흑심", "address": "전북 전주시 완산구 전라감영2길 27-1 1층"},
    {"id": 10, "name": "태평집", "address": "전북 전주시 완산구 전라감영2길 27-1 1층"},
    {"id": 11, "name": "자매갈비전골", "address": "전북 전주시 완산구 기린대로 121 자매갈비전골"},
    {"id": 12, "name": "다문", "address": "전북 전주시 완산구 은행로 74-8 다문"},
]

def home(request):
    return render(request, 'home/post_list.html')



def reserve(request, pk):

    restaurant = next((r for r in restaurants if r["id"] == pk), None)
    if not restaurant:
        return HttpResponse("해당 식당을 찾을 수 없습니다.", status=404)

    return render(request, 'home/reserve.html', {'restaurant': restaurant})



def reserve_process(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        return HttpResponse(f'예약 완료! 이름: {name}, 날짜: {date}')
    return HttpResponse('잘못된 요청입니다.', status=400)



class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post