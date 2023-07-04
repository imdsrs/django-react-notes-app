from django.shortcuts import render

# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
from .utils import updateNote, getNoteDetail, deleteNote, getNoteList, createNote

# Create your views here.


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {
            "Endpoint": "/notes/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of notes",
        },
        {
            "Endpoint": "/notes/id",
            "method": "GET",
            "body": None,
            "description": "Returns a single note object",
        },
        {
            "Endpoint": "/notes/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "Creates new note with data sent in post request",
        },
        {
            "Endpoint": "/notes/id/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "Creates an existing note with data sent in post request",
        },
        {
            "Endpoint": "/notes/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "Deletes and exiting note",
        },
    ]
    return Response(routes)


# /notes GET
# /notes PUT
# /notes/<id> GET
# /notes/<id> PUT
# /notes/<id> DELETE


@api_view(["GET", "POST"])
def getNotes(request):
    if request.method == "GET":
        return getNoteList(request)
        # notes = Note.objects.all().order_by("-created")
        # serializer = NoteSerializer(notes, many=True)
        # return Response(serializer.data)
    if request.method == "POST":
        return createNote(request)
        # data = request.data
        # note = Note.objects.create(body=data["body"])
        # serializer = NoteSerializer(note, many=False)
        # return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def getNote(request, pk):
    if request.method == "GET":
        # paramID = request.GET.get('id') ##to get param from /note?id=2
        # note = Note.objects.get(id=pk)
        # serializer = NoteSerializer(note, many=False)
        # return Response(serializer.data)
        return getNoteDetail(request, pk)
    if request.method == "PUT":
        # data = request.data
        # note = Note.objects.get(id=pk)
        # serializer = NoteSerializer(instance=note, data=data)

        # if serializer.is_valid():
        #     serializer.save()

        # return Response(serializer.data)
        print("try update")
        return updateNote(request, pk)
    if request.method == "DELETE":
        return deleteNote(request, pk)
        # note = Note.objects.get(id=pk)
        # note.delete()
        # return Response("The note was deleted!")


# @api_view(["POST"])
# def createNote(request):
#     data = request.data
#     note = Note.objects.create(body=data["body"])
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)


# @api_view(["PUT"])
# def updateNote(request, pk):
#     data = request.data
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance=note, data=data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(["DELETE"])
# def deleteNote(request, pk):
#     note = Note.objects.get(id=pk)
#     note.delete()
#     return Response("The note was deleted!")
