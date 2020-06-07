
const LOCAL_DOMAINS = ["localhost", "127.0.0.1"];
if (LOCAL_DOMAINS.includes(window.location.hostname)) {
    document.getElementById("authorize-button").setAttribute("onclick", "location.href = 'https://www.strava.com/oauth/authorize?client_id=36057&redirect_uri=http://127.0.0.1:8000/exchange_code&response_type=code&approval_prompt=auto&scope=activity:read;'")
} else {
    document.getElementById("authorize-button").setAttribute("onclick", "location.href = 'https://www.strava.com/oauth/authorize?client_id=36057&redirect_uri=http://nickdoornekamp.pythonanywhere.com/exchange_code&response_type=code&approval_prompt=auto&scope=activity:read;'")
}
