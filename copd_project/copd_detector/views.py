from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .predictor import make_prediction

def detect_copd_view(request):
    context = {}
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'audio_file' in request.FILES:
            uploaded_file = request.FILES['audio_file']
            
            # Use FileSystemStorage to save the file temporarily
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            
            # Get the full path to the saved file
            uploaded_file_path = fs.path(filename)
            
            # Get the URL to access the file from the browser
            uploaded_file_url = fs.url(filename)
            
            # Make a prediction
            predicted_class, confidence = make_prediction(uploaded_file_path)
            
            # Add results to the context
            context['prediction'] = predicted_class
            context['confidence'] = f"{confidence:.2%}"
            context['uploaded_file_url'] = uploaded_file_url
            
            # Optional: You can delete the file after prediction if you want
            # fs.delete(filename)
        else:
            context['error'] = "No audio file was uploaded."

    return render(request, 'index.html', context)