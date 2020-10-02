from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from login import models as loginModel
from meeting import models as meetingModel
from datetime import datetime
import copy
import os
# Create your views here.
def home_view(request):
	if request.user.is_authenticated:
		request.session['MeetingInFocus'] = None
		if request.method == "POST":
			if 'create_new_meeting' in request.POST:
				return redirect('create_new_meeting_view')
			else:
				key_list = list(request.POST.keys())
				values_list = list(request.POST.values())
				meeting_ID = key_list[values_list.index('')]
				request.session['MeetingInFocus'] = meeting_ID 
				return redirect('meeting_view')

		context = {
			'administratorStatus' : False
		}

		currentUser = loginModel.User.objects.get(username=request.user.username)
		
		meetings_list = meetingModel.meeting.objects.all().order_by("-createdOn")
		context['meetings_list'] = meetings_list

		if currentUser.administratorStatus:
			context['administratorStatus'] = True

		return render(request, 'home.html', context)
	else:
		return redirect('login_view')

def create_new_meeting_view(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			meeting_header = request.POST['meeting_header']
			start_time_string = request.POST['startTime']
			end_time_string = request.POST['endTime']
			start_time = datetime(int(start_time_string[0:4]),
				int(start_time_string[5:7]),
				int(start_time_string[8:10]),
				int(start_time_string[11:13]),
				int(start_time_string[14:]))
			
			end_time = datetime(int(end_time_string[0:4]),
				int(end_time_string[5:7]),
				int(end_time_string[8:10]),
				int(end_time_string[11:13]),
				int(end_time_string[14:]))
		
			newMeeting = meetingModel.meeting.objects.create(meetingHeader=meeting_header, startTime=start_time, endTime=end_time)
			newMeeting.save()

			return redirect('home_view')


		return render(request, 'newMeeting.html')
	else:
		return redirect('login_view')
	

def meeting_view(request):
	if request.user.is_authenticated:

		current_meeting_id = request.session['MeetingInFocus']
		current_meeting_object = meetingModel.meeting.objects.get(id=current_meeting_id)

		current_user = loginModel.User.objects.get(username=request.user.username)

		agenda_items_for_current_meeting = []
		agenda_items_with_relevant_comments =[]

		for item in meetingModel.agendaItem.objects.all():
			if item.underMeeting == current_meeting_object:
				agenda_items_for_current_meeting.append(item)

		temporary_holder_dict = {}
		copy_of_holder = {}

		for item in agenda_items_for_current_meeting:
			temporary_holder_dict[item] = []
			for comment in meetingModel.comment.objects.all():
				if comment.underAgendaItem == item:
					temporary_holder_dict[item].append(comment)
			copy_of_holder = copy.deepcopy(temporary_holder_dict)
			agenda_items_with_relevant_comments.append(copy_of_holder)
			temporary_holder_dict = {}

		

		context = {
		'meeting_object' : current_meeting_object,
		'administratorStatus' : False,
		'agenda_items_for_current_meeting': agenda_items_for_current_meeting,
		'agenda_items_with_relevant_comments': agenda_items_with_relevant_comments
		}

		if current_user.administratorStatus:
			context['administratorStatus'] = True

		return render(request, 'meeting.html', context)
	else:
		return redirect('login_view')
	


def create_new_agenda_item(request):
	current_meeting_id = request.session['MeetingInFocus']
	current_meeting_object = meetingModel.meeting.objects.get(id=current_meeting_id)
	if request.method == "POST":
		agenda_item_header = request.POST['agenda_header']
		agenda_item_background = request.POST['agenda_background']
		meetingModel.agendaItem.objects.create(underMeeting=current_meeting_object,
			agendaHeader=agenda_item_header,
		 	agendaMainText=agenda_item_background)

	return HttpResponse()

def create_new_comment_item(request):
	if request.method == "POST":
		current_user = loginModel.User.objects.get(username=request.user.username)
		current_agenda_item = meetingModel.agendaItem.objects.get(id=request.POST['agenda_id'])
		meetingModel.comment.objects.create(author=current_user, 
			underAgendaItem=current_agenda_item,
			text=request.POST['comment_text'])
	return HttpResponse()

def account_view(request):
	if request.user.is_authenticated:
		return render(request, 'account.html')
	else:
		return redirect('login_view')

def change_password_view(request):
	if request.method == 'POST':
		current_user = loginModel.User.objects.get(username=request.user.username)
		current_password = request.POST['current_password']
		user_authentication = authenticate(request, username=current_user.username, password=current_password)
		if user_authentication is not None:
			if request.POST['new_password_1'] == request.POST['new_password_2']:
				current_user.set_password(request.POST['new_password_1'])
				current_user.save()
				login(request, current_user)
				return HttpResponse()
			else:
				return HttpResponse()
		else:
			return HttpResponse()
