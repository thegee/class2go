from django.http import HttpResponsefrom django.shortcuts import render_to_responsefrom django.template import Context, loaderfrom django.template import RequestContextdef admin(request, course_id):    return render_to_response('courses/admin.html', {'course_id': course_id, 'request': request}, context_instance=RequestContext(request))    def staff(request, course_id):    return render_to_response('courses/staff.html', {'course_id': course_id, 'request': request}, context_instance=RequestContext(request))    def new(request):    return render_to_response('courses/new.html', {'request': request}, context_instance=RequestContext(request))