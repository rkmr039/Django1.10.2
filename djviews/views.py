from django.http import HttpResponse, HttpResponseRedirect 


# def home(request):
# 	print(request)
# 	print(dir(request))
# 	print(request.get_full_path())
# 	return HttpResponse("<!DOCTYPE>\
# 		<html>\
# 			<head>\
# 				<style>h1 {color:red}</style>\
# 			</head>\
# 			<body>\
# 				<h1>Hello World with ResponseObject directly</h1>\
# 			</body>\
# 		</html>\
# 		")

def home(request):
	response = HttpResponse(content_type='text/html')

	response.write("<!DOCTYPE>\
 		<html>\
 			<head>\
 				<style>h1 {color:red}</style>\
 			</head>\
 			<body>\
 				<h1>Hello World with ResponseObject inderictly </h1>\
 			</body>\
 		</html>\
		")
	

	if(response.status_code == 404):
		print("Page not found")

	response.content = 'New Contents'
	response.write("Another Response Object after new content")
	return response

def redirect_somewhere(request):
	return HttpResponseRedirect("/some/path")