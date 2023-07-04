from .serializers import NoteSerializer
from .models import Note
from rest_framework.response import Response


def getNoteList(request):
    notes = Note.objects.all().order_by("-created")
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


def createNote(request):
    data = request.data
    note = Note.objects.create(body=data["body"])
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def getNoteDetail(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def updateNote(request, pk):
    print("try update 2")
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("The note was deleted!")
