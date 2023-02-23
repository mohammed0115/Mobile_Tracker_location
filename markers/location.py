import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def get_location1(request):
    ip_address = get_client_ip(request)
    print(ip_address)
    response = requests.get(f"https://ipapi.co/{ip_address}/json/")
    response=response.json()
    # location_data = {
    #    "ip": ip_address,
    #    "lat": response.get("latitude"),
    #    "lng": response.get("longitude"),
    #    "country": response.get("country_name")
    # }
    return response
def get_location():
    ip_address = get_ip()
    print(ip_address)
    response = requests.get(f"https://ipapi.co/{ip_address}/json/")
    response=response.json()
    # location_data = {
    #    "ip": ip_address,
    #    "lat": response.get("latitude"),
    #    "lng": response.get("longitude"),
    #    "country": response.get("country_name")
    # }
    return response
    # return "data"

# print(get_location())