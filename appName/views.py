from django.shortcuts import render, HttpResponse
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import ctypes

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Create your views here.
def wordcloud2(request):
    if request.method=="POST":
        print("\nTHIS IS POST")
        name = request.POST['nameBox']
        paragraph = request.POST['textBox']
        print("NAME IS", name)
        # print("PARAGRAPH IS", paragraph)
        wordcloud = WordCloud(width=screensize[0], height=screensize[1]).generate(paragraph)
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.show()
        plt.savefig('D:\.capturesByGameBar\img1.png' , dpi = 500 , facecolor='blue')
        wordcloud.to_file("D:\.capturesByGameBar\img2.png")

    return render(request , 'home.html')
