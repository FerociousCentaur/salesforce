CLIENT_ID = "3MVG9fe4g9fhX0E5_wv8mgdqGgAFlBseQM5BDgndVgL81.SUeZSNI1kjODmd0_y_f.tFEiJ80tJOOB_fsrRT9"

SECRET_ID = "59A44954666DD025232373A39698406796F141D0AAA1AF2DF2DF051C19D1B113"
RETURN_URL = "http://localhost/"
SDFC_USER = "vivekanand@iitmadras.com"
PASSWORD = "Postman1@2"

URL = "https://login.salesforce.com/services/oauth2/token"



# def homepage(request):
#
#     data = {
#     'client_id': settings.CLIENT_ID,
#     'client_secret':settings.SECRET_ID,
#     'grant_type':'password',
#     'username':settings.SDFC_USER,
#     'password':settings.PASSWORD
#     }
#
#     response = requests.post(settings.URL,data=data)
#     json_res = response.json()
#     print(json_res)
#     access_token = json_res['access_token']
#     auth = {'Content_type':'application/json',
#     'Accept_Encoding':'gzip',
#     'Authorization':"Bearer %s"% access_token}
#     instance_url = json_res['instance_url']
#
#     url2= instance_url+"/services/data/v45.0/query/"
#     params = {'q':'SELECT * from Contacts'}
#     res = requests.get(url2 ,headers = auth,params = params)
#     r = res.json()
#     print(r)