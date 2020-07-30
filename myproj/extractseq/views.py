from django.shortcuts import render
from django.shortcuts import HttpResponse

from .forms import ExtractseqForm

from .extseqs import extseqs

# Create your views here.

def index(request):
    form = ExtractseqForm()
    context = {
        'form':form
    }
    return render(request,'extractseq/index.html',context=context)

def extractseq(request):
    if request.method == "POST":
        sequences = request.POST['sequences']
        seqids = request.POST['seqids']
        outfile = request.POST['filename']
        print(seqids)
        output_seq = extseqs(sequences,seqids)
        print(output_seq)
        response_content = ''.join(output_seq)
        print(response_content)
        response = HttpResponse(response_content,content_type="text/plain,chartset=utf8")
        response['Content-Disposition'] = 'attachment;filename={}'.format(outfile)
        return response

        #return HttpResponse('<h1>OK</h1>')