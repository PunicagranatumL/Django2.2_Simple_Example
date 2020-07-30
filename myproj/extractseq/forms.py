from django import forms

class ExtractseqForm(forms.Form):
    sequences = forms.CharField(
        label="Paste your sequences here",
        max_length=20000,
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':">Seq1\nATCGA\n>Seq2\nATGCCA",
            }
        )
    )
    seqids = forms.CharField(
        label="Paste your seq id here",
        max_length=20000,
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':"Seq1\nSeq2\n",
            }
        )
    )
    filename = forms.CharField(
        label="input the name of output file",
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'output.fasta',
            }
        )
    )
