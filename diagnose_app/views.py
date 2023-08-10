from django.shortcuts import render, redirect

MOVES = { (0, 0, 0): { 'name' : 'レインメーカー', 'url' : 'https://www.youtube.com/embed/oN3WPWr4HKE' },
          (0, 0, 1): { 'name' : 'GTR', 'url' : 'https://www.youtube.com/embed/7352fEHDZZI' },
          (0, 1, 0): { 'name' : 'ストームブレイカー', 'url' : 'https://www.youtube.com/embed/7B7yNCdrx0E' },
          (0, 1, 1): { 'name' : 'デスティーノ', 'url' : 'https://www.youtube.com/embed/kO_fKzX-00o' },
          (1, 0, 0): { 'name' : 'ハイフライフロー', 'url' : 'https://www.youtube.com/embed/_sXN7Ft8Hvg' },
          (1, 0, 1): { 'name' : 'アルティマウェポン', 'url' : 'https://www.youtube.com/embed/YWBi0BFL9Ag' },
          (1, 1, 0): { 'name' : 'ジャベ・インモルタル', 'url' : 'https://www.youtube.com/embed/XmuPDccVUCo' },
          (1, 1, 1): { 'name' : 'ヌメロ・ドス', 'url' : 'https://www.youtube.com/embed/P594OnCK2P8' },
}


# Create your views here.
def topfunc(request):
    if request.method == "POST":
        print('-----')

        print(request.POST.get("q1"))
        print(answers(request))
        print(str(answers(request)))
        print(MOVES[answers(request)])
        

        return redirect('/result?answers=' + str(answers(request)))

    return render(request, 'top.html')

def answers(post_request):
    q1 = 0 if post_request.POST.get("q1") == "打撃、投げ" else 1
    q2 = 0 if post_request.POST.get("q2") == "パワー系" else 1
    q3 = 0 if post_request.POST.get("q3") == "スター性" else 1

    return (q1, q2, q3)
 
def resultfunc(request):
    answers = eval(request.GET.get('answers'))
    result = MOVES[answers]

    print(type(answers))
    print(MOVES[answers])
    
    return render(request, 'result.html', {'name': result['name'], 'url': result['url']})