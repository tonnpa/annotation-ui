/**
 * Created by tonnpa on 12/9/16.
 */
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function prepRequest(request) {
    request.dataType = "json";
    request.contentType = "application/json";
    return request;
}